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

def _gemini_translate(korean_items: list[str], target_lang: str, lang_desc: str, mode: str = "list") -> list[str]:
    """
    (제미나이 API 삭제됨 - 에이전트가 직접 번역 수행해야 함)
    현재는 미번역 태그만 달아서 반환합니다.
    """
    return [f"[번역 필요 / {target_lang.upper()}] {item}" for item in korean_items]


def _sync_action_guides(ko_guides: dict, existing_lang_guides: dict, lang: str, lang_desc: str, force: bool = False) -> dict:
    """
    action_guides (structured dict) 동기화
    KO의 각 키를 해당 언어로 번역합니다. 이중 딕셔너리도 지원합니다.
    """
    result = {}
    for key, ko_items in ko_guides.items():
        if isinstance(ko_items, dict):
            existing_sub = existing_lang_guides.get(key, {})
            if not isinstance(existing_sub, dict):
                existing_sub = {}
            result[key] = _sync_action_guides(ko_items, existing_sub, lang, lang_desc, force)
            continue
        
        # list인 경우
        existing = existing_lang_guides.get(key, [])
        if not isinstance(existing, list):
            existing = []
            
        if not force and len(existing) == len(ko_items) and not any(isinstance(t, str) and "[번역 필요" in t for t in existing):
            print(f"    ✅ [{lang.upper()}] structured.{key}: 이미 동기화됨 ({len(existing)}개)")
            result[key] = existing
        else:
            print(f"    🔄 [{lang.upper()}] structured.{key}: 번역 중... ({len(ko_items)}개)")
            # 100개씩 번역 시 Gemini 에러 방지를 위해 30개 단위 분배
            translated_list = []
            chunk_size = 30
            for i in range(0, len(ko_items), chunk_size):
                chunk = ko_items[i:i+chunk_size]
                chunk_trans = _gemini_translate(chunk, lang, lang_desc)
                translated_list.extend(chunk_trans)
            result[key] = translated_list
    return result


def _sync_list(ko_items: list, existing_items: list, lang: str, lang_desc: str, section_name: str, force: bool = False) -> list:
    """
    일반 목록(list) 동기화
    """
    if not force and len(existing_items) == len(ko_items) and not any("[번역 필요" in t for t in existing_items):
        print(f"    ✅ [{lang.upper()}] {section_name}: 이미 동기화됨 ({len(existing_items)}개)")
        return existing_items
    
    print(f"    🔄 [{lang.upper()}] {section_name}: 번역 중... ({len(ko_items)}개)")
    return _gemini_translate(ko_items, lang, lang_desc)


def _write_updated_i18n(data: dict):
    """
    업데이트된 I18N_DATA를 saju_i18n.py에 저장합니다.
    백업 파일을 먼저 생성하고, 필요한 임포트와 유틸리티 함수를 보존합니다.
    """
    # 1. 기존 파일에서 CONTEXT_MAPS 추출 (없으면 빈 딕셔너리 또는 기본값)
    context_maps_str = "{}"
    try:
        content = I18N_FILE.read_text(encoding="utf-8")
        match = re.search(r"CONTEXT_MAPS\s*=\s*({.*?})\s*I18N_DATA", content, re.DOTALL)
        if match:
            context_maps_str = match.group(1)
        else:
            # 직접 정의 시도 (백업 등에서 가져온 현재 상태 유지)
            import saju_i18n
            if hasattr(saju_i18n, 'CONTEXT_MAPS'):
                context_maps_str = json.dumps(saju_i18n.CONTEXT_MAPS, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"  ⚠️ CONTEXT_MAPS 추출 실패: {e}")

    # 2. 백업
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = I18N_FILE.with_suffix(f".backup_{timestamp}.py")
    backup_path.write_text(I18N_FILE.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"  📦 백업 생성: {backup_path.name}")
    
    # 3. 새 파일 작성 (헤더 + CONTEXT_MAPS + 데이터 + 푸터)
    header = "from typing import Dict, Any, List\n\n"
    footer = textwrap.dedent("""
    def get_localized_data(lang: str) -> Dict[str, Any]:
        \"\"\"요청된 언어의 데이터를 반환하며, 없을 경우 한국어('ko')를 기본값으로 사용합니다.\"\"\"
        return I18N_DATA.get(lang, I18N_DATA.get('ko', {}))
    """)
    
    output_lines = [
        header,
        f"# 자동 생성: i18n_sync_agent.py ({datetime.now().strftime('%Y-%m-%d %H:%M')})",
        "# ⚠️ 이 파일을 직접 수정하지 마세요. 한국어(ko) 섹션만 수정하고 sync 스크립트를 실행하세요.",
        "",
        f"CONTEXT_MAPS = {context_maps_str}",
        "",
        "I18N_DATA = " + json.dumps(data, ensure_ascii=False, indent=4),
        "",
        footer
    ]
    
    I18N_FILE.write_text("\n".join(output_lines), encoding="utf-8")
    print(f"  ✅ saju_i18n.py 업데이트 완료 (CONTEXT_MAPS 보존)")


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
                updated = _sync_action_guides(ko_target, existing, lang, lang_desc, force)
            else:
                updated = _sync_list(ko_target, existing, lang, lang_desc, f"{top_key}.{sub_key}", force)
            
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
