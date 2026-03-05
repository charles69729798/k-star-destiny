"""
ES/PT 섹션에 TIP_COMPONENTS와 MISSION_COMPONENTS를 삽입하는 스크립트
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from multi_agent_translation_0301 import TRANSLATIONS

i18n_path = os.path.join(os.path.dirname(__file__), '..', 'backend', 'saju_i18n.py')

with open(i18n_path, 'r', encoding='utf-8') as f:
    content = f.read()


def make_tip_mission_block(lang_data: dict, indent: int = 8) -> str:
    """TIP_COMPONENTS + MISSION_COMPONENTS 파이썬 딕셔너리 문자열 생성"""
    pad = " " * indent
    pad2 = " " * (indent + 4)
    pad3 = " " * (indent + 8)
    pad4 = " " * (indent + 12)

    def q(s):
        return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'

    def list_block(lst, indent_str):
        items = ",\n".join([f"{indent_str}    {q(x)}" for x in lst])
        return f"[\n{items}\n{indent_str}]"

    lines = []
    # TIP_COMPONENTS
    lines.append(f'{pad}"TIP_COMPONENTS": {{')
    lines.append(f'{pad2}"actions": {list_block(lang_data["TIP_ACTIONS"], pad2)},')
    lines.append(f'{pad2}"topics": {list_block(lang_data["TIP_TOPICS"], pad2)},')
    lines.append(f'{pad2}"results": {list_block(lang_data["TIP_RESULTS"], pad2)}')
    lines.append(f'{pad}}},')

    # MISSION_COMPONENTS
    lines.append(f'{pad}"MISSION_COMPONENTS": {{')
    lines.append(f'{pad2}"labels": {list_block(lang_data["MISSION_LABELS"], pad2)},')
    lines.append(f'{pad2}"reasons": {list_block(lang_data["MISSION_REASONS"], pad2)},')
    lines.append(f'{pad2}"tasks": {{')
    lines.append(f'{pad3}"vibe": {list_block(lang_data["MISSION_TASKS_VIBE"], pad3)},')
    lines.append(f'{pad3}"heart": {list_block(lang_data["MISSION_TASKS_HEART"], pad3)},')
    lines.append(f'{pad3}"energy": {list_block(lang_data["MISSION_TASKS_ENERGY"], pad3)}')
    lines.append(f'{pad2}}}')
    lines.append(f'{pad}}}')

    return "\n".join(lines)


def insert_before_pattern(content: str, pattern: str, insertion: str) -> str:
    """패턴 앞에 삽입"""
    idx = content.find(pattern)
    if idx == -1:
        return content
    return content[:idx] + insertion + "\n" + content[idx:]


# ────────────────────────────────────
# EN 섹션: 이미 TIP_COMPONENTS 존재 → 생략
# ES 섹션: SYNERGY_MISSIONS 직전에 삽입
# PT 섹션: SYNERGY_MISSIONS 직전에 삽입
# ────────────────────────────────────

# ES 섹션
es_start = content.find('"es":')
pt_start = content.find('"pt":')
ko_start = content.find('"ko":')

# ES 섹션 내부의 SYNERGY_MISSIONS 위치 찾기
es_synergy_pattern = '"SYNERGY_MISSIONS"'
# ES와 PT 사이에서 탐색
es_section  = content[es_start:pt_start]
es_synergy_rel = es_section.find(es_synergy_pattern)

if es_synergy_rel != -1:
    es_synergy_abs = es_start + es_synergy_rel
    # 삽입 위치: SYNERGY_MISSIONS 앞 줄 앞
    es_block = make_tip_mission_block(TRANSLATIONS["es"], indent=8)
    content = content[:es_synergy_abs] + es_block + ",\n        " + content[es_synergy_abs:]
    print("✅ ES 섹션에 TIP_COMPONENTS + MISSION_COMPONENTS 삽입 완료")
else:
    print("⚠️ ES 섹션에서 SYNERGY_MISSIONS 위치를 찾지 못했습니다.")

# PT 섹션 (ES 삽입 후 새로고침)
pt_start = content.find('"pt":')
ko_start = content.find('"ko":')
pt_section = content[pt_start:ko_start]
pt_synergy_rel = pt_section.find('"SYNERGY_MISSIONS"')

if pt_synergy_rel != -1:
    pt_synergy_abs = pt_start + pt_synergy_rel
    pt_block = make_tip_mission_block(TRANSLATIONS["pt"], indent=8)
    content = content[:pt_synergy_abs] + pt_block + ",\n        " + content[pt_synergy_abs:]
    print("✅ PT 섹션에 TIP_COMPONENTS + MISSION_COMPONENTS 삽입 완료")
else:
    print("⚠️ PT 섹션에서 SYNERGY_MISSIONS 위치를 찾지 못했습니다.")

# 저장
with open(i18n_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n💾 saju_i18n.py 저장 완료 (총 {len(content):,} bytes)")
print("🎉 EN/ES/PT 모두 TIP_COMPONENTS + MISSION_COMPONENTS 동기화 완료!")
