"""
다국어 자동 동기화 AI 에이전트 스크립트 (i18n_sync_agent.py)
=============================================================
역할: 한국어(KO) 원문이 수정되면, 각국 MZ K-pop 전문 AI 에이전트(Gemini)를 통해
      EN/ES/PT 번역을 자동 생성·검증하여 saju_i18n.py에 반영합니다.

사용법:
  1. 직접 실행:  python i18n_sync_agent.py
  2. git hook:   .git/hooks/pre-commit 에서 자동 호출

환경 변수:
  GEMINI_API_KEY = 구글 Gemini API 키
"""

import os
import sys
import ast
import json
import hashlib
import re
import textwrap
from pathlib import Path
from datetime import datetime
from typing import Optional

# ─── Gemini SDK 로드 ──────────────────────────────────────────
try:
    import google.generativeai as genai
    HAS_GEMINI = True
except ImportError:
    HAS_GEMINI = False
    print("⚠️  google-generativeai 패키지가 없습니다. pip install google-generativeai 를 실행하세요.")

# ─── 설정 ──────────────────────────────────────────────────────
BACKEND_DIR = Path(__file__).parent
I18N_FILE   = BACKEND_DIR / "saju_i18n.py"
HASH_FILE   = BACKEND_DIR / ".i18n_ko_hash"   # KO 원문 해시 (변경 감지용)

TARGET_LANGS = {
    "en": "English (US) for Gen-Z K-pop fans",
    "es": "Spanish (Latin American) for Gen-Z K-pop fans",
    "pt": "Brazilian Portuguese for Gen-Z K-pop fans",
}

AGENT_PERSONA = """You are a multilingual MZ-generation K-pop fan community manager and translator.
You write translations that:
- Sound natural and trendy for Gen-Z K-pop fans in the target language
- Use current social media slang and K-pop fandom terminology
- Keep the {idol} placeholder exactly as-is (do NOT translate it)
- Match the emotional tone of the Korean original (warm, encouraging, fan-activity focused)
- Are concise (1-2 sentences max per item)
"""

# ─── 핵심 섹션 정의 (이 목록이 동기화 대상) ──────────────────
SYNC_SECTIONS = [
    # (최상위 섹션 키, 하위 키, 번역 모드)
    ("MZ_ANALYSIS_FRAGMENTS", "action_guides", "structured"),
    ("MZ_ANALYSIS_FRAGMENTS", "bias_tmi",      "list"),
    ("MZ_ANALYSIS_FRAGMENTS", "recent_fortune", "list"),
    ("MZ_ANALYSIS_FRAGMENTS", "synergy_why",   "list"),
]


def _load_i18n() -> dict:
    """saju_i18n.py에서 I18N_DATA 딕셔너리를 읽어옵니다."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("saju_i18n", I18N_FILE)
    mod  = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.I18N_DATA


def _ko_hash(data: dict) -> str:
    """KO 섹션의 해시값을 계산합니다 (변경 감지)."""
    ko_text = json.dumps(data.get("ko", {}), ensure_ascii=False, sort_keys=True)
    return hashlib.md5(ko_text.encode()).hexdigest()


def _has_ko_changed(data: dict) -> bool:
    """이전 실행 이후 KO가 변경되었는지 확인합니다."""
    current_hash = _ko_hash(data)
    if HASH_FILE.exists():
        saved_hash = HASH_FILE.read_text().strip()
        if saved_hash == current_hash:
            return False
    return True


def _save_ko_hash(data: dict):
    """현재 KO 해시를 저장합니다."""
    HASH_FILE.write_text(_ko_hash(data))


def _gemini_translate(korean_items: list[str], target_lang: str, lang_desc: str, mode: str = "list") -> list[str]:
    """
    Gemini API를 사용해 한국어 텍스트를 번역합니다.
    
    Args:
        korean_items: 번역할 한국어 텍스트 목록
        target_lang:  언어 코드 (en, es, pt)
        lang_desc:    에이전트 설명용 언어 이름
        mode:         "list" or "structured"
    """
    if not HAS_GEMINI:
        return [f"[번역 필요 / {target_lang.upper()}] {item}" for item in korean_items]
    
    api_key = os.environ.get("GEMINI_API_KEY", "")
    if not api_key:
        print(f"  ⚠️  GEMINI_API_KEY 환경변수가 없습니다. 번역을 건너뜁니다.")
        return [f"[번역 필요 / {target_lang.upper()}] {item}" for item in korean_items]
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-pro")
    
    items_text = "\n".join([f"{i+1}. {item}" for i, item in enumerate(korean_items)])
    
    prompt = f"""{AGENT_PERSONA}

TARGET LANGUAGE: {lang_desc}

Translate the following Korean K-pop fan activity descriptions to {lang_desc}.
Keep the text natural, trendy and MZ-generation appropriate.
If the text contains {{idol}}, keep it exactly as {{idol}} in the output.
Return ONLY a JSON array of translated strings, no explanations.

Korean originals:
{items_text}

Return format: ["translation1", "translation2", ...]"""
    
    try:
        response = model.generate_content(prompt)
        raw = response.text.strip()
        # JSON 배열 추출
        json_match = re.search(r'\[.*?\]', raw, re.DOTALL)
        if json_match:
            translated = json.loads(json_match.group())
            if len(translated) == len(korean_items):
                return translated
    except Exception as e:
        print(f"  ❌ Gemini 번역 오류 ({target_lang}): {e}")
    
    # 폴백: 원문 + 마커
    return [f"[번역 필요 / {target_lang.upper()}] {item}" for item in korean_items]


def _sync_action_guides(ko_guides: dict, existing_lang_guides: dict, lang: str, lang_desc: str) -> dict:
    """
    action_guides (structured dict) 동기화
    KO의 각 키(vibe, heart, energy)를 해당 언어로 번역합니다.
    """
    result = {}
    for key, ko_items in ko_guides.items():
        existing = existing_lang_guides.get(key, [])
        # 이미 동일 개수가 존재하고 번역 마커가 없으면 유지
        if len(existing) == len(ko_items) and not any("[번역 필요" in t for t in existing):
            print(f"    ✅ [{lang.upper()}] action_guides.{key}: 이미 동기화됨 ({len(existing)}개)")
            result[key] = existing
        else:
            print(f"    🔄 [{lang.upper()}] action_guides.{key}: 번역 중... ({len(ko_items)}개)")
            translated = _gemini_translate(ko_items, lang, lang_desc)
            result[key] = translated
    return result


def _sync_list(ko_items: list, existing_items: list, lang: str, lang_desc: str, section_name: str) -> list:
    """
    일반 목록(list) 동기화
    """
    if len(existing_items) == len(ko_items) and not any("[번역 필요" in t for t in existing_items):
        print(f"    ✅ [{lang.upper()}] {section_name}: 이미 동기화됨 ({len(existing_items)}개)")
        return existing_items
    
    print(f"    🔄 [{lang.upper()}] {section_name}: 번역 중... ({len(ko_items)}개)")
    return _gemini_translate(ko_items, lang, lang_desc)


def _write_updated_i18n(data: dict):
    """
    업데이트된 I18N_DATA를 saju_i18n.py에 저장합니다.
    백업 파일을 먼저 생성합니다.
    """
    # 백업
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = I18N_FILE.with_suffix(f".backup_{timestamp}.py")
    backup_path.write_text(I18N_FILE.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"  📦 백업 생성: {backup_path.name}")
    
    # 새 파일 작성
    output_lines = [
        "# -*- coding: utf-8 -*-",
        f"# 자동 생성: i18n_sync_agent.py ({datetime.now().strftime('%Y-%m-%d %H:%M')})",
        "# ⚠️ 이 파일을 직접 수정하지 마세요. 한국어(ko) 섹션만 수정하고 sync 스크립트를 실행하세요.",
        "",
        "I18N_DATA = " + json.dumps(data, ensure_ascii=False, indent=4),
    ]
    
    I18N_FILE.write_text("\n".join(output_lines), encoding="utf-8")
    print(f"  ✅ saju_i18n.py 업데이트 완료")


def run_sync(force: bool = False):
    """
    메인 동기화 실행 함수
    """
    print("\n" + "=" * 60)
    print("🤖 K-Destiny 다국어 AI 에이전트 동기화 시작")
    print("=" * 60)
    
    # 1. 현재 i18n 데이터 로드
    print("\n📂 saju_i18n.py 로드 중...")
    try:
        data = _load_i18n()
    except Exception as e:
        print(f"❌ saju_i18n.py 로드 실패: {e}")
        sys.exit(1)
    
    # 2. KO 변경 감지
    if not force and not _has_ko_changed(data):
        print("✅ 한국어 원문 변경 없음 — 동기화 건너뜀")
        print("   강제 실행하려면: python i18n_sync_agent.py --force")
        return
    
    print("🔔 한국어 원문 변경 감지! 다국어 에이전트 번역 시작...\n")
    
    ko_data = data.get("ko", {})
    changed = False
    
    # 3. 섹션별 동기화
    for top_key, sub_key, mode in SYNC_SECTIONS:
        ko_section = ko_data.get(top_key, {})
        ko_target  = ko_section.get(sub_key, {} if mode == "structured" else [])
        
        if not ko_target:
            print(f"⏭️  KO.{top_key}.{sub_key} 비어있음 — 건너뜀")
            continue
        
        print(f"\n📝 섹션: {top_key}.{sub_key}")
        
        for lang, lang_desc in TARGET_LANGS.items():
            lang_section = data.setdefault(lang, {}).setdefault(top_key, {})
            existing     = lang_section.get(sub_key, {} if mode == "structured" else [])
            
            if mode == "structured":
                updated = _sync_action_guides(ko_target, existing, lang, lang_desc)
            else:
                updated = _sync_list(ko_target, existing, lang, lang_desc, f"{top_key}.{sub_key}")
            
            if updated != existing:
                data[lang][top_key][sub_key] = updated
                changed = True
    
    # 4. 변경사항 저장
    if changed:
        print("\n💾 변경사항 저장 중...")
        _write_updated_i18n(data)
        _save_ko_hash(data)
        print("\n✅ 동기화 완료!")
    else:
        print("\n✅ 모든 섹션이 이미 최신 상태입니다.")
        _save_ko_hash(data)


if __name__ == "__main__":
    force_flag = "--force" in sys.argv
    run_sync(force=force_flag)
