import re

file_path = 'c:/InsuranceProject/Sajuapp/backend/saju_engine.py'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# We need to find the definition of analyze_destiny and rewrite the part where it fetches the descriptions
# Let's target the lines:
# 1. `month_data_src = MONTH_DESCS`
# 2. `chem_src_style = PURE_LOVE_STYLES if pure_mode else LOVE_STYLES`
# 3. `chem_src_synergy = PURE_SYNERGY if pure_mode else ELEMENT_SYNERGY`
# 4. `chem_src_tips = PURE_TIPS if pure_mode else TIPS`
# 5. The base string inside `generate_monthly_fortune`: actually kwargs passed to it.

new_analyze_destiny = """    # 언어 화일 적용
    i18n_data = get_localized_data(lang)
    
    # 텍스트 리소스 선택 (lang)
    if i18n_data:
        month_descs_data = i18n_data.get("MONTH_DESCS", MONTH_DESCS)
        love_styles_data = i18n_data.get("PURE_LOVE_STYLES" if pure_mode else "LOVE_STYLES", PURE_LOVE_STYLES if pure_mode else LOVE_STYLES)
        element_synergy_data = i18n_data.get("PURE_SYNERGY" if pure_mode else "ELEMENT_SYNERGY", PURE_SYNERGY if pure_mode else ELEMENT_SYNERGY)
        tips_data = i18n_data.get("PURE_TIPS" if pure_mode else "TIPS", PURE_TIPS if pure_mode else TIPS)
    else:
        month_descs_data = MONTH_DESCS
        love_styles_data = PURE_LOVE_STYLES if pure_mode else LOVE_STYLES
        element_synergy_data = PURE_SYNERGY if pure_mode else ELEMENT_SYNERGY
        tips_data = PURE_TIPS if pure_mode else TIPS

    month_data_src = month_descs_data
    chem_src_style = love_styles_data
    chem_src_synergy = element_synergy_data
    chem_src_tips = tips_data"""

# Using regex to replace the old assignments in analyze_destiny
pattern = r"""    i18n_data = get_localized_data\(lang\)\n.*?chem_src_tips = PURE_TIPS if pure_mode else TIPS"""

if re.search(pattern, content, flags=re.DOTALL):
    content = re.sub(pattern, new_analyze_destiny, content, flags=re.DOTALL)
    print("Pattern matched and substituted!")
else:
    print("Pattern NOT found. Let's do a more robust replace.")
    # Fallback to pure string replace based on what's there
    old_fragment = """    # 언어 화일 적용
    i18n_data = get_localized_data(lang)
    
    # 월별 운세 텍스트 (다국어 미지원 시 기본 한글 MONTH_DESCS 사용)
    month_data_src = MONTH_DESCS
    
    # 궁합 텍스트 (순수 모드 vs MBTI 모드 분리)
    chem_src_style = PURE_LOVE_STYLES if pure_mode else LOVE_STYLES
    chem_src_synergy = PURE_SYNERGY if pure_mode else ELEMENT_SYNERGY
    chem_src_tips = PURE_TIPS if pure_mode else TIPS"""
    if old_fragment in content:
        content = content.replace(old_fragment, new_analyze_destiny)
        print("Fallback exact string matched and substituted!")
    else:
        print("Fallback exact string also NOT found.")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
