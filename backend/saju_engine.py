from typing import Dict, Any
import random
import re
from datetime import datetime
from saju_i18n import get_localized_data, CONTEXT_MAPS
from saju_rules import MBTI_CHEMISTRY, ELEMENT_CREATION_MAP, SYNERGY_SCORE_RANGES

# ──────────────────────────────────────────────
# 1. K-사주 오행 별 심층 텍스트 베이스 (Soul Index) - KO Default
# ──────────────────────────────────────────────
# Note: All data constants (ENERGY_TRAITS, MONTH_DESCS, etc.) have been moved to saju_i18n.py

def context_aware_replace(text: str, context_map: dict) -> str:
    """정규표현식을 사용하여 긴 문구부터 우선적으로 치환합니다 (맥락 보존)."""
    if not text or not context_map:
        return text
    # 키들을 길이 역순으로 정렬하여 긴 문구가 먼저 매칭되도록 함
    sorted_keys = sorted(context_map.keys(), key=len, reverse=True)
    pattern = re.compile('|'.join(re.escape(k) for k in sorted_keys))
    return pattern.sub(lambda m: context_map[m.group(0)], text)

def get_element_relation(e1: str, e2: str) -> str:
    if e1 == e2: return "HARMONY"
    if ELEMENT_CREATION_MAP.get(e1) == e2 or ELEMENT_CREATION_MAP.get(e2) == e1: return "CREATE"
    return "CONTROL"

def get_mbti_quad_description(mbti: str, lang: str = "ko") -> list:
    """MBTI 4개 기능을 조합하여 분자 수준의 성격 묘사를 생성합니다."""
    loc = get_localized_data(lang)
    UI = loc.get("UI_STRINGS", {})
    
    # MBTI 정보가 없을 경우 오행 기반 기본 묘사 반환
    if not mbti or len(mbti) != 4:
        return [UI.get("mbti_unknown_desc", "신비로운 잠재력을 지닌 에너지가 느껴집니다.")]
        
    mbti_fragments = loc.get("MBTI_FUNC_FRAGMENTS", {})
    if not mbti_fragments:
        return []
        
    m = mbti.upper()
    descriptions = []
    
    # E/I, N/S, T/F, J/P 순서로 조립
    mapping = [("e_i", 0), ("n_s", 1), ("t_f", 2), ("j_p", 3)]
    for key, idx in mapping:
        fragment = mbti_fragments.get(key, {}).get(m[idx], "")
        if fragment: descriptions.append(fragment)
    
    return descriptions

def generate_scientific_hypothesis(weights: Dict[str, int], mbti: str, lang: str = "ko", is_user: bool = False) -> str:
    """오행 가중치와 MBTI를 결합하여 정밀 가설을 생성합니다 (RPRE 엔진)."""
    if not weights or not mbti:
        return ""
        
    loc = get_localized_data(lang)
    UI = loc.get("UI_STRINGS", {})
    
    # MBTI가 없는 경우 기본값 할당 (분석 누락 방지)
    mbti_val = mbti if mbti else UI.get("mbti_unrevealed", "Secret")
    
    rpre_key = "RPRE_TEMPLATES_USER" if is_user else "RPRE_TEMPLATES"
    rpre_data = loc.get(rpre_key, loc.get("RPRE_TEMPLATES", {}))
    if not rpre_data: return ""
    
    primary = max(weights.keys(), key=lambda k: weights[k])
    # 가중치에 따른 성격 뉘앙스 (Top 2)
    sorted_weights = sorted(weights.items(), key=lambda x: x[1], reverse=True)
    p1, p2 = sorted_weights[0][0], sorted_weights[1][0]
    
    # 무작위 템플릿 선택으로 독창성 확보
    t_id = random.choice(list(rpre_data.keys())) if rpre_data else "core_v1"
    template = rpre_data.get(t_id, "{p1}의 본질에 {p2}의 재능이 더해진 당신.")
    return template.format(p1=p1, p2=p2, mbti=mbti_val, element=primary)

import hashlib

def _hash_seed(text: str) -> int:
    """단순 합산 방식에서 SHA-256 기반 고도화 해시로 변경하여 충돌 최소화"""
    return int(hashlib.sha256(text.encode()).hexdigest(), 16)

def _det_pick(key: str, pool: list):
    """풀에서 언어가 달라도 동일한 인덱스 항목을 결정론적으로 선택합니다.
    동일 key → 동일 인덱스 → 언어별 병렬 pool에서 같은 번째 항목 반환"""
    if not pool:
        return ""
    idx = _hash_seed(key) % len(pool)
    return pool[idx]

def calc_element_weights(date_str: str) -> Dict[str, int]:
    """연, 월, 일의 분포를 기반으로 5행 가중치를 계산합니다 (100% 환산)."""
    elements = ["Wood", "Fire", "Earth", "Metal", "Water"]
    try:
        # YYYY-MM-DD-HH 형식 처리
        d = datetime.strptime(date_str[:10], "%Y-%m-%d")
    except:
        return {el: 20 for el in elements} # 에러 발생 시 균등 분배
        
    sc = {el: 10 for el in elements} # 기본값 (보정)
    
    # 가중치 부여 (청사진 기준)
    # 연(Year): 근본 (20점)
    sc[elements[d.year % 5]] += 20
    # 월(Month): 환경/성격 (30점)
    sc[elements[d.month % 5]] += 30
    # 일(Day): 자아/일간 (40점)
    sc[elements[d.day % 5]] += 40
    
    # 100% 비율로 정규화
    total = sum(sc.values())
    normalized = {k: int((v / total) * 100) for k, v in sc.items()}
    
    # 합계가 100이 안될 경우 보정 (최대값에 추가)
    diff = 100 - sum(normalized.values())
    if diff != 0:
        max_key = max(normalized.keys(), key=lambda k: normalized[k])
        normalized[max_key] += diff
        
    return normalized

def calc_dominant(date_str: str) -> str:
    """가장 가중치가 높은 지배 오행을 반환합니다."""
    weights = calc_element_weights(date_str)
    return max(weights.keys(), key=lambda k: weights[k])

def generate_monthly_fortune(keywords, descs, seed_val: str = None, month_names: list = None) -> list:
    if seed_val:
        random.seed(_hash_seed(seed_val))
    
    monthly = []
    
    if not keywords or not descs:
        return []
    
    # We now have exactly 12 items for each to ensure sequence integrity
    for i in range(12):
        k = keywords[i] if i < len(keywords) else keywords[-1]
        
        # Enhanced Randomness: Handle expanded flat list by using seed-based offset
        if isinstance(descs, list) and len(descs) > 12 and not isinstance(descs[0], list):
            # Pick a unique index from the large flat list
             offset = random.randint(0, len(descs) // 12 - 1)
             d_idx = (i + offset * 12) % len(descs)
             d = descs[d_idx]
        else:
            d_pool = descs[i] if i < len(descs) else descs[-1]
            if isinstance(d_pool, list):
                d = random.choice(d_pool)
            else:
                d = d_pool
            
        if month_names and i < len(month_names):
            m_str = month_names[i]
        else:
            m_str = str(i+1)
            
        monthly.append({
            "month": m_str,
            "keyword": k,
            "desc": d
        })
    
    return monthly

def get_segmented_fortune(dominant: str, segments: dict, seed_val: str = None) -> str:
    """인생 주기를 초년, 청년, 중년, 말년으로 세분화하여 반환합니다."""
    if seed_val:
        random.seed(_hash_seed(seed_val))
    
    if not segments or dominant not in segments:
        return UI.get("analyzing_data", "사주 데이터 분석 중...")
        
    s = segments[dominant]
    # 명리학적으로 유의미한 변주를 위해 세그먼트별로 약간의 수식어 추가 가능 (현재는 정기 데이터 반환)
    stages = [
        s.get("youth", ""),
        s.get("young_adult", ""),
        s.get("middle_age", ""),
        s.get("senior", "")
    ]
    
    return "\n\n".join([stage for stage in stages if stage])

def calculate_synergy_score(e1, e2, u_birth, i_birth, u_mbti, i_mbti) -> int:
    rel = get_element_relation(e1, e2)
    base_min, base_max = SYNERGY_SCORE_RANGES.get(rel, (70, 90))
    
    seed_val = f"CHEM_SCORE_{e1}_{e2}_{u_birth}_{i_birth}"
    random.seed(_hash_seed(seed_val))
    score = random.randint(base_min, base_max)
    
    # Parity adjustment (+2 if same year parity)
    try:
        if u_birth[:4].isdigit() and i_birth[:4].isdigit():
            if int(u_birth[:4]) % 2 == int(i_birth[:4]) % 2:
                score += 2
    except: pass
    
    # MBTI formal adjustment (Algorithm-based)
    if u_mbti and i_mbti:
        u_m = u_mbti.upper().strip()
        i_m = i_mbti.upper().strip()
        # Fallback for matching E/I if full MBTI not in matrix
        if u_m in MBTI_CHEMISTRY and i_m in MBTI_CHEMISTRY[u_m]:
            score += MBTI_CHEMISTRY[u_m][i_m]
        elif u_m[0] == i_m[0]:
            score += 3
        
    return min(100, score)

def filter_missions_by_element(missions, element, seed_val: str = None) -> list:
    if seed_val:
        random.seed(_hash_seed(seed_val))
        
    if not missions: return []
    
    tag_map = {
        "Fire": ["[Viral]", "[Challenge]", "[Party]", "[Cafe]", "[Karaoke]", "[Adrenaline]", "[Passion]", "[Rhythm]", "[Busking]"],
        "Water": ["[Chill]", "[Zen]", "[Bookworm]", "[Secret]", "[Quiet]", "[Lake]", "[Aquarium]", "[Meditation]", "[Disconnect]"],
        "Earth": ["[Foodie]", "[Nature]", "[Camping]", "[Zoo]", "[Garden]", "[Bakery]", "[Picnic]", "[Street Food]", "[Market]"],
        "Wood": ["[Growth]", "[Grind]", "[Aesthetic]", "[Style]", "[Vlog]", "[Glow-up]", "[Photography]", "[Custom]", "[4-cut]", "[Fashion]"],
        "Metal": ["[Luxury]", "[Art]", "[Tech]", "[Museum]", "[History]", "[Gallery]", "[Castle]", "[Modern Art]", "[Architecture]"]
    }
    
    preferred_tags = tag_map.get(element, [])
    # Filter missions that have at least one preferred tag
    filtered = [m for m in missions if any(tag in str(m) for tag in preferred_tags)]
    
    # If not enough filtered missions, use original set
    source = filtered if len(filtered) >= 3 else missions
    selected = random.sample(source, min(3, len(source)))
    
    return selected

def assemble_mz_report(fragments: dict, user_el: str, idol_el: str, user_mbti: str, idol_mbti: str, score: int, idol_name: str, lang: str = "ko", UI: dict = None, user_name: str = "You", is_friend: bool = False, partner_word: str = "스타") -> dict:
    """하드코딩 배제: 조각들을 조합하여 5문장 이상의 디테일한 MZ 리포트 생성
    ✅ 언어에 관계없이 동일한 내용(인덱스)이 선택되도록 _det_pick() 사용"""
    # 결정론적 시드 키 (언어 제외 → 언어마다 같은 항목 선택)
    base_key = f"MZ_REPORT_D5_{user_el}_{idol_el}_{user_mbti}_{idol_mbti}_{score}_{idol_name}"
    
    # 1. Relationship (Intro + Core)
    rel_type = get_element_relation(user_el, idol_el)
    rel_labels = UI.get("REL_LABELS", {}) if UI else {}
    intro_pool = fragments.get("relationship_intro", ["{score}%"])
    intro_tpl = _det_pick(f"{base_key}_intro", intro_pool)
    intro = intro_tpl.format(score=score, rel_label=rel_labels.get(rel_type, rel_type))
    
    core_raw = fragments.get("relationship_core", [""])
    if isinstance(core_raw, list):
        core = _det_pick(f"{base_key}_core", core_raw)
    else:
        core = core_raw.get(rel_type, "")
    relationship = f"{intro} {core}"
    
    # 2. Bias Analysis (5-sentence Synthesis: Essence + Point + Growth + Aura + TMI)
    essence = _det_pick(f"{base_key}_ess", fragments.get("bias_essence", [""])).format(element=idol_el)
    point = _det_pick(f"{base_key}_pt", fragments.get("bias_point", [""]))
    growth = _det_pick(f"{base_key}_growth", fragments.get("bias_growth", [""]))
    aura = _det_pick(f"{base_key}_aura", fragments.get("bias_aura", [""]))
    
    # 3. MBTI TMI
    mbti_traits = UI.get("MBTI_TRAITS", {})
    trait_desc = mbti_traits.get(
        idol_mbti[0].upper() if idol_mbti and idol_mbti != 'Unknown' else 'E',
        UI.get("mysterious_label", "신비로운")
    )
    bias_tmi = _det_pick(f"{base_key}_tmi", fragments.get("bias_tmi", [""])).format(
        mbti=idol_mbti, mbti_trait=trait_desc,
        user=user_name, idol=idol_name,
        u_el=user_el, i_el=idol_el,
        u_mbti=user_mbti, i_mbti=idol_mbti
    )
    
    # Combined Bias Description (5 sentences)
    bias_desc = f"{essence} {point} {growth} {aura} {bias_tmi}"
    
    # 4. Recent Fortune (이제 미션 섹션의 상단 동기부여 '명분'으로 활용됨)
    recent = _det_pick(f"{base_key}_fortune", fragments.get("recent_fortune", [UI.get("default_fortune_msg", "빛나는 하루!")])).format(
        idol=idol_name, user=user_name,
        u_el=user_el, i_el=idol_el,
        u_mbti=user_mbti, i_mbti=idol_mbti
    )
    
    # 5. Synergy Why
    synergy_why = _det_pick(f"{base_key}_why", fragments.get("synergy_why", [""])).format(
        u_element=user_el, i_element=idol_el, 
        u_mbti=user_mbti, i_mbti=idol_mbti,
        user=user_name, idol=idol_name,
        u_el=user_el, i_el=idol_el
    )
    
    # [MZ UX 고도화] 최근 운세 정보를 미션 섹션의 'Context'로 최상단 배치하도록 유도
    scan_label = UI.get("aura_scan_label", "Aura Scan") if not is_friend else UI.get("friend_scan_label", "Friend Scan")
    mission_motivation = f"🎮 [{idol_name} {scan_label}]\n{recent}\n\n{synergy_why}"
    
    # 결과 리포트 딕셔너리 초기화
    report_dict = {
        "relationship": relationship,
        "bias": bias_desc,
        "bias_list": [essence, point, growth, aura, bias_tmi],
        "tmi": bias_tmi,
        "recentFortune": recent,
        "synergyWhy": synergy_why,
        "missionMotivation": mission_motivation,
        "actionGuides": fragments.get("action_guides", {})
    }

    if is_friend:
        # [맥락 인지형 치환 엔진] saju_i18n의 CONTEXT_MAPS를 사용하여 스타 전용 용어를 지인/친구 용어로 변환
        lang_context = CONTEXT_MAPS.get(lang, CONTEXT_MAPS.get("ko", {}))
        
        # 정렬하여 긴 단어부터 치환 (부분 일치 방지)
        sorted_keys = sorted(lang_context.keys(), key=len, reverse=True)
        
        # partner_word(친구/지인 등) 반영
        final_context = lang_context.copy()
        if lang == "ko":
            final_context["스타"] = partner_word
            final_context["스타가"] = f"{partner_word}가"
            final_context["스타는"] = f"{partner_word}는"
            final_context["스타를"] = f"{partner_word}를"
            final_context["스타의"] = f"{partner_word}의"
            final_context["스타와"] = f"{partner_word}와"

        for k in sorted_keys:
            v = final_context[k]
            # 문자열 필드 전역 치환
            for field in ["relationship", "bias", "tmi", "recentFortune", "synergyWhy", "missionMotivation"]:
                if field in report_dict:
                    report_dict[field] = report_dict[field].replace(k, v)
            
            # 리스트 필드 치환
            report_dict["bias_list"] = [item.replace(k, v) for item in report_dict["bias_list"]]
            
            # actionGuides (중첩 딕셔너리) 치환
            if "actionGuides" in report_dict:
                for category in report_dict["actionGuides"]:
                    if isinstance(report_dict["actionGuides"][category], list):
                        report_dict["actionGuides"][category] = [
                            item.replace(k, v) if isinstance(item, str) else item 
                            for item in report_dict["actionGuides"][category]
                        ]

    return report_dict

# ──────────────────────────────────────────────
# 메인 분석 엔진
# ──────────────────────────────────────────────
def analyze_destiny(
    birth_date_str: str, 
    gender: str = "female", 
    user_mbti: str = "", 
    idol_name: str = "", 
    idol_mbti: str = "", 
    idol_birth_date: str = "",
    lang: str = "ko",
    is_friend: bool = False
) -> Dict[str, Any]:
    try:
        user_saju = None
        monthly_fortune = None
        chemistry_signal = None
        lifetime_fortune = None
        
        loc = get_localized_data(lang)
        
        L_ENERGY_TRAITS = loc.get("ENERGY_TRAITS", {})
        L_MONTH_KEYWORDS = loc.get("MONTH_KEYWORDS", [])
        L_MONTH_DESCS = loc.get("MONTH_DESCS", [])
        L_LIFETIME_STAGES = loc.get("LIFETIME_STAGES", {})
        L_LOVE_STYLES = loc.get("LOVE_STYLES", [])
        L_ELEMENT_SYNERGY = loc.get("ELEMENT_SYNERGY", {})
        L_TIPS = loc.get("TIPS", [])
        L_ELEMENT_LABELS = loc.get("ELEMENT_LABELS", {})
        UI = loc.get("UI_STRINGS", {})
        fragments = loc.get("MZ_ANALYSIS_FRAGMENTS", {})

        dominant = calc_dominant(birth_date_str)
        user_weights = calc_element_weights(birth_date_str) # Next-Gen 가중치 분석
        
        # idol_dominant 일찍 정의 (NameError 방지)
        idol_dominant = calc_dominant(idol_birth_date) if idol_birth_date else None
        
        user_el = UI.get("element_labels", {}).get(dominant, dominant)
        idol_el = UI.get("element_labels", {}).get(idol_dominant, idol_dominant) if idol_dominant else user_el
        
        trait = L_ENERGY_TRAITS.get(dominant, L_ENERGY_TRAITS.get("Earth")) # Fallback to Earth

        # Use birth date for deterministic user fortune
        user_seed = f"{birth_date_str}{gender}"
        random.seed(_hash_seed(user_seed))
        
        user_mbti_str = user_mbti if user_mbti else UI.get("mbti_unrevealed", "Secret")
        user_mbti_logic = get_mbti_quad_description(user_mbti, lang) # MBTI 4자 분자 분석
        user_rpre = generate_scientific_hypothesis(user_weights, user_mbti, lang, is_user=True) # RPRE 가설 생성
        
        mbti_e_i = "default"
        if user_mbti and len(user_mbti) > 0 and user_mbti.upper()[0] in ['E', 'I']:
            mbti_e_i = user_mbti.upper()[0]

        display_user = UI.get("user_name_fallback", "You")
        
        # 모듈 조립 및 동적 바인딩
        c_intro_raw = random.choice(trait.get('desc_intro', [""])) if isinstance(trait.get('desc_intro'), list) else trait.get('desc_intro', '')
        c_intro = c_intro_raw.format(user=display_user)
        
        # MBTI 4자 분석 결과 반영 (잠재력 섹션 보강)
        mbti_core = " ".join(user_mbti_logic) if user_mbti_logic else ""
        c_core_pool = trait.get('desc_core', {}).get(mbti_e_i, trait.get('desc_core', {}).get('default', [""]))
        if not c_core_pool or isinstance(c_core_pool, str): c_core_pool = [c_core_pool]
        c_core_raw = random.choice(c_core_pool)
        c_core = c_core_raw.format(user=display_user)
        
        c_career_raw = random.choice(trait.get('desc_career', [""])) if isinstance(trait.get('desc_career'), list) else trait.get('desc_career', '')
        c_career = c_career_raw.format(user=display_user)
        
        c_advice_raw = random.choice(trait.get('desc_advice', [""])) if isinstance(trait.get('desc_advice'), list) else trait.get('desc_advice', '')
        c_advice = c_advice_raw.format(user=display_user)

        # 오행 가중치 요약 문구 생성
        weight_summary = ", ".join([f"{UI.get('element_labels', {}).get(k, k)} {v}%" for k, v in user_weights.items() if v > 10])

        user_saju_content = (
            f"📊 {UI.get('scientific_analysis', 'Scientific Analysis')}\n"
            f"- {UI.get('element_weight', 'Element Weights')}: {weight_summary}\n"
            f"- {UI.get('mbti_dynamic', 'MBTI Dynamics')}: {mbti_core}\n\n"
            f"🔬 {UI.get('rpre_hypothesis', 'Persona Hypothesis')}\n{user_rpre}\n\n"
            f"✨ {UI.get('signature', 'Signature')}\n{c_intro}\n\n"
            f"💡 {UI.get('potential', 'Potential')}\n{c_core}\n\n"
            f"🚀 {UI.get('guide', 'Guide')}\n{c_advice}"
        )
        
        user_saju = {
            "summary": trait["name"],
            "element": dominant,
            "elements": user_weights, # 시각화 게이지용 데이터 추가
            "content": user_saju_content
        }

        partner_word = UI.get("friend_word", "Friend") if is_friend else UI.get("star_word", "Star")
        
        display_idol = idol_name if idol_name else partner_word
        display_user = UI.get("user_name_fallback", "You")

        # 2026 Monthly Fortune (3-Layer Analysis)
        monthly_fortune = []
        L_MONTH_FORTUNES = loc.get("MONTH_FORTUNES", {})
        
        for m in range(1, 13):
            m_str = str(m)
            m_data = L_MONTH_FORTUNES.get(m_str, {})
            
            # 사주적 연산 가미 (간단한 시너지 점수 시뮬레이션)
            m_seed = f"{user_seed}_MONTH_{m}"
            random.seed(_hash_seed(m_seed))
            m_score = random.randint(60, 95)
            
            # 데이터 치환 및 확장
            theme = m_data.get("theme", "").format(dominant=dominant)
            signal = m_data.get("signal", "").format(idol=display_idol)
            guide = m_data.get("guide", "").format(dominant=dominant)
            
            monthly_fortune.append({
                "month": m,
                "score": m_score,
                "synergy": m_score, # 프론트엔드에서 기대하는 키 추가
                "theme": theme,
                "signal": signal,
                "star_signal": signal,
                "guide": guide,
                "action_point": guide,
                # 하위 호환성을 위한 원본 필드 유지 (조합형)
                "keyword": theme.split(' ')[0], 
                "desc": f"{theme} {signal} {guide}"
            })

        # Theory-Grounded Segmented Lifetime Fortune
        lifetime_fortune = get_segmented_fortune(dominant, L_LIFETIME_STAGES, seed_val=f"SEGMENTED_{user_seed}")
        
        # MBTI 누락 여부에 따른 컨텍스트 이원화
        is_pure_saju = not idol_mbti or idol_mbti == 'Unknown' or idol_mbti == UI.get("mbti_unrevealed")
        
        if is_pure_saju:
            L_CUR_LOVE = loc.get("PURE_LOVE_STYLES", [])
            L_CUR_SYN = loc.get("PURE_SYNERGY", {})
            L_CUR_TIPS = loc.get("PURE_TIPS", [])
            idol_mbti_fallback = UI.get("pure_saju_label", "🌟 Deep Soul Ripple")
        else:
            L_CUR_LOVE = L_LOVE_STYLES
            L_CUR_SYN = L_ELEMENT_SYNERGY
            L_CUR_TIPS = L_TIPS
            idol_mbti_fallback = idol_mbti if idol_mbti else UI.get("mbti_unrevealed")
        
        # Deterministic Chemistry Seed
        chem_seed = f"{birth_date_str}{gender}{idol_name}{idol_birth_date}"
        random.seed(_hash_seed(chem_seed))
        
        if idol_dominant:
            rel = get_element_relation(dominant, idol_dominant)
            synergy_text_raw = L_CUR_SYN.get(rel, "")
            synergy_text = synergy_text_raw.format(user=display_user, idol=display_idol)
        else:
            synergy_text_raw = random.choice(list(L_CUR_SYN.values())) if L_CUR_SYN else ""
            synergy_text = synergy_text_raw.format(user=display_user, idol=display_idol)
        
        # Dynamic Synergy Missions (Context-Aware 3x3 Structure)
        missions_raw = loc.get("SYNERGY_MISSIONS", {})
        base_score = calculate_synergy_score(dominant, idol_dominant if idol_dominant else dominant, birth_date_str, idol_birth_date if idol_birth_date else birth_date_str, user_mbti, idol_mbti)
        
        # 꿀팁/미션 유니크성 강화를 위한 결정론적 시드 설정 (완전한 언어 독립적 시드)
        sampling_key = f"MISSION_{user_seed}_{dominant}_{user_mbti}_{idol_name}_{base_score}"
        random.seed(_hash_seed(sampling_key))

        # MISSION_COMPONENTS (고도화된 조합형 데이터) 우선 참조
        mission_frags = loc.get("GEN_MISSION_COMPONENTS", {})
        if not mission_frags:
            mission_frags = loc.get("MISSION_COMPONENTS", loc.get("SYNERGY_MISSIONS", loc.get("MISSION_FRAGMENTS", {})))
            
        m_labels = mission_frags.get("labels", ["Analysis {n}"])
        m_reasons = mission_frags.get("reasons", ["Due to {u_el} & {i_el} synergy"])
        m_tasks_pool = mission_frags.get("tasks", {})

        def f_str(s, idx=1, target=""):
            if not s: return ""
            # 친구 모드일 경우 스타/팬 용어를 지인/친구 용어로 치환
            if is_friend:
                lang_context = CONTEXT_MAPS.get(lang, CONTEXT_MAPS.get("ko", {}))
                final_context = lang_context.copy()
                if lang == "ko":
                    final_context.update({
                        "스타": partner_word,
                        "스타가": f"{partner_word}가", "스타는": f"{partner_word}는",
                        "스타를": f"{partner_word}를", "스타의": f"{partner_word}의", "스타와": f"{partner_word}와"
                    })
                s = context_aware_replace(s, final_context)
            
            # 오행에 따른 인덱스 추출 (Wood:0, Fire:1, Earth:2, Metal:3, Water:4)
            el_idx_map = {"Wood": 0, "Fire": 1, "Earth": 2, "Metal": 3, "Water": 4}
            idx_v = el_idx_map.get(dominant, 0)
            
            # MZ 성향 키워드 추출
            u_mbti_trait = UI.get("mbti_trait_map", {}).get(user_mbti, "독창적인")
            
            # rel_type 지역화 (상생, 상극, 조화)
            s_labels = UI.get("SYNERGY_LABELS", {"생": "상생", "극": "상극", "조화": "조화"})
            raw_type = "생" if base_score > 70 else "극" if base_score < 40 else "조화"
            rel_type = s_labels.get(raw_type, s_labels.get("조화"))
            
            # 리스트 구조 대응: trait_map, place_map
            trait_pool = UI.get("trait_map", ["매력"])
            place_pool = UI.get("place_map", ["장소"])
            # 리스트일 경우 인덱스로 접근, 아닐 경우(구형) .get() 시도
            cur_trait = trait_pool[idx_v] if isinstance(trait_pool, list) else trait_pool.get(dominant, "매력")
            cur_place = place_pool[idx_v] if isinstance(place_pool, list) else place_pool.get(dominant, "장소")

            # 아이돌 그룹명 추출 (하드코딩 제거용)
            i_group = UI.get("star_word", "아이돌") if not is_friend else partner_word
            if not is_friend and idol_name:
                # 간단한 그룹명 추정 로직 (예: 에스파 카리나 -> 에스파)
                parts = display_idol.split()
                if len(parts) > 1: i_group = parts[0]
                else: i_group = display_idol

            return s.format(
                user=display_user, idol=display_idol, n=idx, idx=idx,
                u_mbti=user_mbti if user_mbti else UI.get("mbti_unrevealed", "Secret"),
                i_mbti=idol_mbti_fallback if idol_mbti_fallback else UI.get("mbti_unrevealed", "Secret"),
                mbti=user_mbti if user_mbti else UI.get("mbti_unrevealed", "Secret"),
                u_el=user_el, i_el=idol_el,
                target=target,
                idol_group=i_group, i_group=i_group,
                trait=cur_trait,
                place=cur_place,
                organ=UI.get("organ_map", {}).get(dominant, "에너지"),
                luck_item=UI.get("luck_item_map", {}).get(dominant, "아이템"),
                star=UI.get("star_map", {}).get(dominant, "별자리"),
                skill=UI.get("skill_map", {}).get(dominant, "능력"),
                mbti_trait=u_mbti_trait,
                rel_type=rel_type,
                point=_det_pick(f"{sampling_key}_pt_{idx}", UI.get("MISSION_POINTS", ["특별한"])),
                exercise=UI.get("exercise_map", {}).get(dominant, "운동")
            )

        synergy_missions = []
        is_gen = "GEN_MISSION_COMPONENTS" in loc
        sh_seed = f"SHUFFLE_{user_seed}_{idol_name}"
        
        # Map action guide keys to mission keys
        guide_map = {"vibe": "analysis_1", "heart": "analysis_2", "energy": "analysis_3"}
        
        if is_gen:
            # 알고리즘 기반 파편화 생성 (1,000+ Variations)
            g_actions = mission_frags.get("actions", {}).get(mbti_e_i, mission_frags.get("actions", {}).get("I", []))
            g_targets = mission_frags.get("targets", {}).get(idol_dominant, mission_frags.get("targets", {}).get("Earth", []))
            g_contexts = mission_frags.get("contexts", ["시너지를 극대화하세요."])
            
            # ✅ 중복 제로: label/reason을 셔플 후 순차 pop (Shuffle & Pop 전략)
            sh_seed_gen = f"GEN_SHUFFLE_{user_seed}_{idol_name}"
            m_labels_gen = m_labels.copy()
            m_reasons_gen = m_reasons.copy()
            random.seed(_hash_seed(sh_seed_gen))
            random.shuffle(m_labels_gen)
            random.shuffle(m_reasons_gen)
            
            # 행동(Action) 자체가 겹치지 않도록 9개(혹은 가능한 최대)의 행동을 먼저 무작위 추출
            random.seed(_hash_seed(sampling_key))
            uniq_actions = random.sample(g_actions, 9) if len(g_actions) >= 9 else g_actions
            
            combo_idx = 0
            for m_type, m_key in guide_map.items():
                idx = int(m_key.split('_')[1])
                m_seed_key = f"{sampling_key}_m{idx}"
                
                # 순차 pop으로 중복 0% 보장
                label_tpl = m_labels_gen.pop() if m_labels_gen else f"Mission {idx}"
                reason_tpl = m_reasons_gen.pop() if m_reasons_gen else "Destiny choice"
                
                selected_tasks_detailed = []
                # 테마당 3개의 미션 할당
                for _ in range(3):
                    # 행동은 무조건 겹치지 않게 할당
                    act = uniq_actions[combo_idx % len(uniq_actions)]
                    # 대상과 컨텍스트는 테마 안에서 자연스럽게 섞이도록 랜덤 (결정론적) 추출
                    tgt = _det_pick(f"{m_seed_key}_t{combo_idx}", g_targets)
                    ctx = _det_pick(f"{m_seed_key}_c{combo_idx}", g_contexts)
                    
                    full_task = f"{act} {ctx}"
                    final_sentence = f_str(full_task, idx, target=tgt)
                    
                    # 한국어 문법 호응 자동 교정 (한국어 전용)
                    if lang == "ko":
                        if any(x in final_sentence for x in ['방법입니다', '길입니다', '마법입니다', '퍼즐입니다', '만듭니다', '치트키입니다', '루틴입니다', '비결입니다']):
                            final_sentence = final_sentence.replace('하며 ', '하는 것은 ').replace('갖으며 ', '갖는 것은 ').replace('쓰며 ', '쓰는 것은 ').replace('보내며', '보내는 것은').replace('때리며', '때리는 것은').replace('매며', '매는 것은')
                        elif any(x in final_sentence for x in ['보세요', '하세요']):
                            final_sentence = final_sentence.replace('하는 것은 ', '하며 ').replace('갖는 것은 ', '갖으며 ').replace('쓰는 것은 ', '쓰며 ').replace('보내는 것은', '보내며').replace('때리는 것은', '때리며').replace('매는 것은', '매며')
                            final_sentence = final_sentence.replace('남기는 것은', '남기며').replace('찍는 것은', '찍으며').replace('보태는 것은', '보태며').replace('공유하는 것은', '공유하며').replace('영업하는 것은', '영업하며').replace('참여하는 것은', '참여하며').replace('전하는 것은', '전하며').replace('배포하는 것은', '배포하며').replace('진행하는 것은', '진행하며').replace('상상하는 것은', '상상하며')

                    # 불필요한 공백 치환
                    final_sentence = final_sentence.replace('매력 매력', '매력')
                    final_sentence = final_sentence.replace('  ', ' ')
                    
                    # ✅ 키워드 추출 고도화 (불용어 리스트 대폭 확장)
                    words = final_sentence.split()
                    stopwords = [
                        '스타를', '스타가', '스타의', '나만의', '새벽에', '서로의', '최고의', '강렬한', 
                        '뜨거운', '함께', '통해', '하며', '하는', '위한', '항상', '최애의', '나의', 
                        '너의', '가장', '매우', '진정한', '모든', '각인되는', '만드는', '향한', '담아'
                    ]
                    # 불용어 제외 및 2~4자 핵심 단어 후보 추출
                    candidates = [w.strip('!?,.') for w in words if w not in stopwords and len(w) >= 2]
                    
                    if len(candidates) >= 2:
                        # 두 번째 단어가 명사일 확률이 높음 (첫 단어는 주로 주어/부사)
                        kw = candidates[1] if 2 <= len(candidates[1]) <= 4 else candidates[1][:3]
                    elif candidates:
                        kw = candidates[0][:3]
                    else:
                        kw = "미션"
                    
                    selected_tasks_detailed.append({
                        "task": final_sentence,
                        "keyword": kw
                    })
                    combo_idx += 1
                
                synergy_missions.append({
                    "id": m_key,
                    "label": f_str(label_tpl, idx),
                    "boost": 15 if idx < 3 else 20,
                    "reason": f_str(reason_tpl, idx),
                    "tasks": [t["task"] for t in selected_tasks_detailed],
                    "tasks_detailed": selected_tasks_detailed,
                    "completed": False
                })
        # 2026 Monthly Fortune (3-Layer Analysis)
        monthly_fortune = []
        L_MONTH_FORTUNES = loc.get("MONTH_FORTUNES", {})
        # 오행 한글/로컬 명칭 (프론트엔드 표시용) - 함수 상단에서 정의된 변수 재사용
        el_text = user_el
        idol_el_text = idol_el
        
        for m in range(1, 13):
            m_str = str(m)
            m_data = L_MONTH_FORTUNES.get(m_str, {})
            
            # 사주적 연산 가미 (간단한 시너지 점수 시뮬레이션)
            m_seed = f"{user_seed}_MONTH_{m}"
            random.seed(_hash_seed(m_seed))
            m_score = random.randint(60, 95)
            
            # [맥락 인지형 치환 사전 준비]
            lang_context = CONTEXT_MAPS.get(lang, CONTEXT_MAPS.get("ko", {}))
            final_context = lang_context.copy()
            if lang == "ko" and is_friend:
                final_context["스타"] = partner_word
                final_context["스타가"] = f"{partner_word}가"
                final_context["스타는"] = f"{partner_word}는"
                final_context["스타를"] = f"{partner_word}를"
                final_context["스타의"] = f"{partner_word}의"
                final_context["스타와"] = f"{partner_word}와"
            sorted_keys = sorted(final_context.keys(), key=len, reverse=True)

            # {dominant} 등 플레이스홀더를 실제 오행 텍스트로 치환하여 반환
            raw_theme = m_data.get("theme", "")
            raw_signal = m_data.get("signal", "")
            raw_guide = m_data.get("guide", m_data.get("action_point", ""))

            def render_and_replace(tpl):
                if not tpl: return ""
                try:
                    out = tpl.format(idol=display_idol, user=display_user, dominant=el_text, u_el=user_el, i_el=idol_el)
                except (KeyError, IndexError):
                    out = tpl
                
                if is_friend:
                    for k in sorted_keys:
                        out = out.replace(k, final_context[k])
                return out

            theme_rendered = render_and_replace(raw_theme)
            star_signal = render_and_replace(raw_signal)
            action_point = render_and_replace(raw_guide)

            monthly_fortune.append({
                "month": m,
                "theme": theme_rendered,
                "star_signal": star_signal,
                "action_point": action_point,
                "score": m_score
            })
        

        # 3. Synergy Missions (Fallback: Shuffle & Pop)
        # ✅ is_gen이 False인 경우에만 실행 (GEN_MISSION_COMPONENTS 기반이 아닐 때)
        if not is_gen:
            # 지인 모드면 전용 데이터셋(GEN_MISSION_COMPONENTS_FRIEND), 아니면 기존 i18n 데이터 사용
            # saju_i18n.py에 데이터가 이미 최적화되어 있으므로 로컬 FRIEND_DATA는 제거
            m_comp_key = "GEN_MISSION_COMPONENTS_FRIEND" if is_friend else "GEN_MISSION_COMPONENTS"
            
            # fallback 처리
            mission_frags_sp = loc.get(m_comp_key, loc.get("GEN_MISSION_COMPONENTS", loc.get("MISSION_COMPONENTS", {})))
            m_targets_pool_sp = mission_frags_sp.get("targets", loc.get("MISSION_COMPONENTS", {}).get("targets", {}))

            m_labels_sp = mission_frags_sp.get("labels", ["Mission"]).copy()
            m_reasons_sp = mission_frags_sp.get("reasons", ["Analysis result"]).copy()
            m_tasks_map_sp = mission_frags_sp.get("tasks", {})
            
            # 결정론적 셔플 (언어셋에 관계없이 동일한 순서 보장)
            random.seed(_hash_seed(sh_seed))
            random.shuffle(m_labels_sp)
            random.shuffle(m_reasons_sp)
            
            synergy_missions = []
            point_keys = UI.get("MISSION_POINTS", ["point"])
            
            # 지원 언어 목록
            SUPPORT_LANGS = ["ko", "en", "es", "pt"]
            
            for i in range(1, 4):
                mission_item = {
                    "id": i,
                    "boost": 15 if i < 3 else 20
                }
                
                # 모든 언어에 대해 데이터 생성
                for l in SUPPORT_LANGS:
                    # 해당 언어의 로컬라이즈 데이터 가져오기
                    l_loc = I18N.get(l, I18N["en"])
                    l_UI = l_loc.get("UI_STRINGS", {})
                    
                    if is_friend:
                        # saju_i18n.py에 추가된 _FRIEND 데이터를 우선 사용
                        l_frags = l_loc.get("GEN_MISSION_COMPONENTS_FRIEND", l_loc.get("GEN_MISSION_COMPONENTS", l_loc.get("MISSION_COMPONENTS", {})))
                        l_targets_pool = l_frags.get("targets", l_loc.get("MISSION_COMPONENTS", {}).get("targets", {}))
                    else:
                        l_frags = l_loc.get("GEN_MISSION_COMPONENTS", l_loc.get("MISSION_COMPONENTS", {}))
                        l_targets_pool = l_frags.get("targets", {})
                    
                    l_labels = l_frags.get("labels", ["Mission"]).copy()
                    l_reasons = l_frags.get("reasons", ["Analysis result"]).copy()
                    l_tasks_map = l_frags.get("tasks", {})
                    l_points = l_UI.get("MISSION_POINTS", point_keys)
                    
                    # 시드 고정으로 언어간 동일 항목 선택 보장
                    random.seed(_hash_seed(f"{sh_seed}_LBL_{i}"))
                    l_idx = random.randint(0, len(l_labels)-1) if l_labels else 0
                    label_tpl = l_labels[l_idx] if l_labels else f"Mission {i}"
                    
                    random.seed(_hash_seed(f"{sh_seed}_RSN_{i}"))
                    r_idx = random.randint(0, len(l_reasons)-1) if l_reasons else 0
                    reason_tpl = l_reasons[r_idx] if l_reasons else "Destiny choice"
                    
                    p_key = _det_pick(f"MISSION_PT_{sh_seed}_{i}", l_points)
                    
                    cat = ["vibe", "heart", "energy"][i-1]
                    task_pool = l_tasks_map.get(cat, [f"Challenge {i}"])
                    
                    tgt_list = l_targets_pool.get(idol_dominant, ["special item"])
                    tgt = _det_pick(f"MISSION_TGT_{sh_seed}_{i}", tgt_list)
                    
                    # 과제 선택을 위한 고정 시퀀스 생성
                    selected_task_indices = []
                    pool_size = len(task_pool)
                    for idx_seq in range(3):
                        random.seed(_hash_seed(f"{sh_seed}_TSK_{i}_{idx_seq}"))
                        t_idx = random.randint(0, pool_size - 1) if pool_size > 0 else 0
                        attempts = 0
                        while t_idx in selected_task_indices and pool_size > len(selected_task_indices) and attempts < 10:
                            t_idx = (t_idx + 1) % pool_size
                            attempts += 1
                        selected_task_indices.append(t_idx)
                    
                    l_tasks_raw = [f_str(task_pool[idx], i, tgt) for idx in selected_task_indices if idx < len(task_pool)]
                    
                    f_label = f_str(label_tpl, i, p_key)
                    f_reason = f_str(reason_tpl, i)
                    
                    # 필드명 결정 (기본 언어는 suffix 없음, 나머지는 _lang)
                    suffix = "" if l == lang else f"_{l}"
                    mission_item[f"label{suffix}"] = f_label
                    mission_item[f"reason{suffix}"] = f_reason
                    mission_item[f"tasks{suffix}"] = l_tasks_raw
                    
                    # tasks_detailed는 현재 요청 언어 기준으로만
                    if l == lang:
                        detailed = []
                        for t in l_tasks_raw:
                            parts = t.split(' ', 1)
                            detailed.append({"keyword": parts[0] if len(parts) > 0 else "Mission", 
                                           "task": parts[1] if len(parts) > 1 else t})
                        mission_item["tasks_detailed"] = detailed

                synergy_missions.append(mission_item)

        # MZ Dynamic Analysis Synthesis (5-sentence logic)
        mz_report = assemble_mz_report(
            fragments, dominant, idol_dominant if idol_dominant else dominant, 
            user_mbti, idol_mbti, base_score, idol_name, lang, UI=UI,
            user_name=display_user, is_friend=is_friend, partner_word=partner_word
        )

        # Tips (Deterministic)
        tips_seed = f"TIPS_{sh_seed}_{idol_name}"
        random.seed(_hash_seed(tips_seed))
        selected_tips = random.sample(L_CUR_TIPS, min(3, len(L_CUR_TIPS))) if L_CUR_TIPS else []

        chemistry_signal = {
            "idol_name": idol_name,
            "idol_mbti": idol_mbti_fallback,
            "idol_birth_date": idol_birth_date,
            "idol_detailed_traits": mz_report.get("bias_list", []),
            "relationship": mz_report["relationship"],
            "bias": mz_report["bias"],
            "tmi": mz_report["tmi"],
            "recentFortune": mz_report["recentFortune"],
            "synergyWhy": mz_report["synergyWhy"],
            "missionMotivation": mz_report.get("missionMotivation", ""), # UX 개편 반영
            "synergy": synergy_text,
            "tips": selected_tips,
            "base_synergy_score": base_score,
            "synergy_missions": synergy_missions
        }

        return {
            "dominant_element": dominant,
            "user_saju": user_saju,
            "monthly_fortune": monthly_fortune,
            "lifetime_fortune": lifetime_fortune,
            "chemistry_signal": chemistry_signal,
            "mz_saju_dictionary": loc.get("MZ_SAJU_DICTIONARY", {}),
            "ui_titles": UI.get("TITLES", {}) # 프론트엔드 동적 타이틀 지원
        }
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"Saju MZ Logic Error: {e}")
        return {"error": UI.get("error_msg", "Error in Saju Analysis.") if 'UI' in locals() else "Error in Saju Analysis."}
