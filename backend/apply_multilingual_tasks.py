import json
import re
import sys
import textwrap
from datetime import datetime
from pathlib import Path

# 설정
BASE_DIR = Path("c:/InsuranceProject/k-star-destiny/backend")
I18N_FILE = BASE_DIR / "saju_i18n.py"
STAR_BUNDLE = BASE_DIR / "star_tasks_bundle.json"
FRIEND_BUNDLE = BASE_DIR / "friend_tasks_bundle.json"

def apply():
    print("🚀 다국어 미션 카드 통합 시작...")
    
    # 1. 번들 로드
    with open(STAR_BUNDLE, 'r', encoding='utf-8') as f:
        star_data = json.load(f)
    with open(FRIEND_BUNDLE, 'r', encoding='utf-8') as f:
        friend_data = json.load(f)
        
    # 2. saju_i18n.py 로드 (I18N_DATA 추출)
    sys.path.append(str(BASE_DIR))
    import saju_i18n
    import importlib
    importlib.reload(saju_i18n)
    
    data = saju_i18n.I18N_DATA
    context_maps = saju_i18n.CONTEXT_MAPS
    
    # 3. 데이터 업데이트 (ES, PT)
    for lang in ["es", "pt"]:
        if lang not in data:
            data[lang] = {}
        if "MISSION_COMPONENTS" not in data[lang]:
            data[lang]["MISSION_COMPONENTS"] = {}
        if "tasks" not in data[lang]["MISSION_COMPONENTS"]:
            data[lang]["MISSION_COMPONENTS"]["tasks"] = {}
            
        # Star Tasks 반영
        data[lang]["MISSION_COMPONENTS"]["tasks"]["star_tasks"] = star_data[lang]["star_tasks"]
        # Friend Tasks 반영 
        data[lang]["MISSION_COMPONENTS"]["tasks"]["friend_tasks"] = friend_data[lang]["friend_tasks"]
        
        print(f"  ✅ {lang.upper()} MISSION_COMPONENTS 업데이트 완료")

    # 4. 파일 쓰기 로직 (i18n_sync_agent 스타일)
    context_maps_str = json.dumps(context_maps, ensure_ascii=False, indent=4)
    
    # 백업
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = I18N_FILE.with_suffix(f".backup_merge_{timestamp}.py")
    backup_path.write_text(I18N_FILE.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"  📦 백업 생성: {backup_path.name}")
    
    header = "from typing import Dict, Any, List\n\n"
    footer = textwrap.dedent("""
    def get_localized_data(lang: str) -> Dict[str, Any]:
        \"\"\"요청된 언어의 데이터를 반환하며, 없을 경우 한국어('ko')를 기본값으로 사용합니다.\"\"\"
        return I18N_DATA.get(lang, I18N_DATA.get('ko', {}))
    """)
    
    output_lines = [
        header,
        f"# 자동 생성: apply_multilingual_tasks.py ({datetime.now().strftime('%Y-%m-%d %H:%M')})",
        "# ⚠️ MISSION_COMPONENTS 고품질 번역 통합본이 반영되었습니다.",
        "",
        f"CONTEXT_MAPS = {context_maps_str}",
        "",
        "I18N_DATA = " + json.dumps(data, ensure_ascii=False, indent=4),
        "",
        footer
    ]
    
    I18N_FILE.write_text("\n".join(output_lines), encoding="utf-8")
    print(f"  ✨ {I18N_FILE.name} 최종 업데이트 완료!")

if __name__ == "__main__":
    apply()
