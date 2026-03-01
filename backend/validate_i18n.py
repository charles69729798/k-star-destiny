#!/usr/bin/env python3
"""
i18n 불일치 검증 스크립트 (validate_i18n.py)
=============================================
역할: 한국어(KO) 대비 EN/ES/PT 번역 상태를 검사하여
      개수 불일치·미번역 항목을 리포트합니다.

사용법:
  python validate_i18n.py           # 검사만 실행
  python validate_i18n.py --fix     # 검사 후 자동 번역 동기화 실행
"""
import sys
import json
from pathlib import Path
import importlib.util

BACKEND_DIR = Path(__file__).parent
I18N_FILE   = BACKEND_DIR / "saju_i18n.py"
LANGS       = ["en", "es", "pt"]
CHECK_SECTIONS = [
    ("MZ_ANALYSIS_FRAGMENTS", "action_guides"),
    ("MZ_ANALYSIS_FRAGMENTS", "bias_tmi"),
    ("MZ_ANALYSIS_FRAGMENTS", "recent_fortune"),
    ("MZ_ANALYSIS_FRAGMENTS", "synergy_why"),
]

def _load_i18n() -> dict:
    spec = importlib.util.spec_from_file_location("saju_i18n", I18N_FILE)
    mod  = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.I18N_DATA

def validate():
    print("\n" + "=" * 55)
    print("🔍 K-Destiny 다국어 일치성 검증 리포트")
    print("=" * 55)
    
    data = _load_i18n()
    ko = data.get("ko", {})
    errors = []
    
    for top_key, sub_key in CHECK_SECTIONS:
        ko_val = ko.get(top_key, {}).get(sub_key)
        if ko_val is None:
            continue
        
        # KO 데이터 형태 파악
        if isinstance(ko_val, dict):  # action_guides
            ko_count = {k: len(v) for k, v in ko_val.items()}
        else:
            ko_count = {"(items)": len(ko_val)}
        
        print(f"\n📌 {top_key}.{sub_key}")
        print(f"   KO: {ko_count}")
        
        for lang in LANGS:
            lang_val = data.get(lang, {}).get(top_key, {}).get(sub_key)
            
            if lang_val is None:
                msg = f"   ❌ {lang.upper()}: 번역 없음"
                print(msg)
                errors.append(f"{lang}/{top_key}.{sub_key}: 번역 없음")
                continue
            
            if isinstance(lang_val, dict):
                lang_count = {k: len(v) for k, v in lang_val.items()}
                for k, v in lang_val.items():
                    for item in v:
                        if "[번역 필요" in item:
                            errors.append(f"{lang}/{top_key}.{sub_key}.{k}: 미번역 항목 있음")
            else:
                lang_count = {"(items)": len(lang_val)}
                for item in lang_val:
                    if "[번역 필요" in item:
                        errors.append(f"{lang}/{top_key}.{sub_key}: 미번역 항목 있음")
            
            # 개수 불일치 감지
            mismatch = (ko_count != lang_count)
            status = "⚠️ 개수 불일치" if mismatch else "✅ 정상"
            print(f"   {lang.upper()}: {lang_count}  {status}")
            if mismatch:
                errors.append(f"{lang}/{top_key}.{sub_key}: KO={ko_count} vs {lang.upper()}={lang_count}")
    
    print("\n" + "=" * 55)
    if errors:
        print(f"🚨 총 {len(errors)}개 문제 발견:\n")
        for e in errors:
            print(f"  • {e}")
        print("\n💡 자동 수정: python validate_i18n.py --fix")
        print("   또는:     python i18n_sync_agent.py --force")
        return False
    else:
        print("✅ 모든 언어 번역 일치 확인 완료!")
        return True

if __name__ == "__main__":
    ok = validate()
    if "--fix" in sys.argv and not ok:
        print("\n🔄 i18n_sync_agent.py 자동 실행 중...")
        import subprocess
        subprocess.run([sys.executable, str(BACKEND_DIR / "i18n_sync_agent.py"), "--force"])
    sys.exit(0 if ok else 1)
