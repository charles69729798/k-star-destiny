from typing import Dict, Any
import random
from datetime import datetime
from saju_i18n import get_localized_data
from saju_rules import MBTI_CHEMISTRY, ELEMENT_CREATION_MAP, SYNERGY_SCORE_RANGES

# ──────────────────────────────────────────────
# 1. K-사주 오행 별 심층 텍스트 베이스 (Soul Index) - KO Default
# ──────────────────────────────────────────────
# Note: All data constants (ENERGY_TRAITS, MONTH_DESCS, etc.) have been moved to saju_i18n.py

def get_element_relation(e1: str, e2: str) -> str:
    if e1 == e2: return "HARMONY"
    if ELEMENT_CREATION_MAP.get(e1) == e2 or ELEMENT_CREATION_MAP.get(e2) == e1: return "CREATE"
    return "CONTROL"

def get_mbti_quad_description(mbti: str, lang: str = "ko") -> list:
    """MBTI 4개 기능을 조합하여 분자 수준의 성격 묘서를 생성합니다."""
    if not mbti or len(mbti) != 4:
        return []
    
    loc = get_localized_data(lang)
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

def generate_scientific_hypothesis(weights: Dict[str, int], mbti: str, lang: str = "ko") -> str:
    """오행 가중치와 MBTI를 결합하여 정밀 가설을 생성합니다 (RPRE 엔진)."""
    if not weights or not mbti:
        return ""
        
    loc = get_localized_data(lang)
    rpre_data = loc.get("RPRE_TEMPLATES", {})
    if not rpre_data: return ""
    
    primary = max(weights.keys(), key=lambda k: weights[k])
    # 가중치에 따른 성격 뉘앙스 (Top 2)
    sorted_weights = sorted(weights.items(), key=lambda x: x[1], reverse=True)
    p1, p2 = sorted_weights[0][0], sorted_weights[1][0]
    
    # 무작위 템플릿 선택으로 독창성 확보
    t_id = random.choice(list(rpre_data.keys())) if rpre_data else "core_v1"
    template = rpre_data.get(t_id, "{p1}의 본질에 {p2}의 재능이 더해진 당신.")
    return template.format(p1=p1, p2=p2, mbti=mbti, element=primary)

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
        return "사주 데이터 분석 중..."
        
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

def assemble_mz_report(fragments: dict, user_el: str, idol_el: str, user_mbti: str, idol_mbti: str, score: int, idol_name: str, lang: str = "ko", UI: dict = None, user_name: str = "You") -> dict:
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
    mbti_traits = UI.get("MBTI_TRAITS", {
        'E': '활동적이며 인싸 기질' if lang == "ko" else 'Active and Social',
        'I': '내향적이지만 알찬 갓생러' if lang == "ko" else 'Quiet but Productive',
        'S': '현실적이며 꼼꼼한' if lang == "ko" else 'Realistic and Detail-oriented',
        'N': '상상력 풍부하고 비전 있는' if lang == "ko" else 'Imaginative and Visionary',
        'T': '논리적이고 팩폭 잘하는' if lang == "ko" else 'Logical and Blunt',
        'F': '공감 능력 만렙인' if lang == "ko" else 'Highly Empathetic',
        'J': '계획적이고 철저한' if lang == "ko" else 'Organized and Systematic',
        'P': '자유롭고 호기심 많은' if lang == "ko" else 'Free-spirited and Curious'
    }) if UI else {}
    trait_desc = mbti_traits.get(
        idol_mbti[0].upper() if idol_mbti and idol_mbti != 'Unknown' else 'E',
        "신비로운" if lang == "ko" else "Mysterious"
    )
    bias_tmi = _det_pick(f"{base_key}_tmi", fragments.get("bias_tmi", [""])).format(
        mbti=idol_mbti, mbti_trait=trait_desc,
        user=user_name, idol=idol_name,
        u_el=user_el, i_el=idol_el,
        u_mbti=user_mbti, i_mbti=idol_mbti
    )
    
    # Combined Bias Description (5 sentences)
    bias_desc = f"{essence} {point} {growth} {aura} {bias_tmi}"
    
    # 4. Recent Fortune — 결정론적 선택 (KO와 동일 인덱스 → 의미 일치)
    recent = _det_pick(f"{base_key}_fortune", fragments.get("recent_fortune", ["오늘도 빛나는 하루!"])).format(
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
    
    return {
        "relationship": relationship,
        "bias": bias_desc,
        "bias_list": [essence, point, growth, aura, bias_tmi], # 프론트엔드 호환성을 위한 리스트 추가
        "tmi": bias_tmi,
        "recentFortune": recent,
        "synergyWhy": synergy_why,
        "actionGuides": fragments.get("action_guides", {})
    }

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
    lang: str = "ko"
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
        trait = L_ENERGY_TRAITS.get(dominant, L_ENERGY_TRAITS.get("Earth")) # Fallback to Earth

        # Use birth date for deterministic user fortune
        user_seed = f"{birth_date_str}{gender}"
        random.seed(_hash_seed(user_seed))
        
        user_mbti_str = user_mbti if user_mbti else UI.get("mbti_unrevealed", "Gatekept")
        user_mbti_logic = get_mbti_quad_description(user_mbti, lang) # MBTI 4자 분자 분석
        user_rpre = generate_scientific_hypothesis(user_weights, user_mbti, lang) # RPRE 가설 생성
        
        mbti_e_i = "default"
        if user_mbti and len(user_mbti) > 0 and user_mbti.upper()[0] in ['E', 'I']:
            mbti_e_i = user_mbti.upper()[0]

        display_user = "You" if lang != "ko" else "당신"
        
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
            "content": user_saju_content
        }

        display_user = UI.get("user", "User")
        idol_dominant = calc_dominant(idol_birth_date) if idol_birth_date else None
        idol_loc = L_ENERGY_TRAITS.get(idol_dominant, L_ENERGY_TRAITS.get("Earth")) if idol_dominant else trait
        display_idol = idol_name if idol_name else (UI.get("idol_name_fallback", "아이돌/Idol") if lang == "ko" else "Idol")
        display_user = UI.get("user_name_fallback", "You") if lang != "ko" else "당신"

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
        sampling_key = f"SAMPLING_{user_seed}_{idol_name}_{idol_birth_date}"
        random.seed(_hash_seed(sampling_key))

        # MISSION_COMPONENTS (고도화된 조합형 데이터) 우선 참조
        mission_frags = loc.get("GEN_MISSION_COMPONENTS", {})
        if not mission_frags:
            mission_frags = loc.get("MISSION_COMPONENTS", loc.get("SYNERGY_MISSIONS", loc.get("MISSION_FRAGMENTS", {})))
            
        m_labels = mission_frags.get("labels", ["Analysis {n}"])
        m_reasons = mission_frags.get("reasons", ["Due to {u_el} & {i_el} synergy"])
        m_tasks_pool = mission_frags.get("tasks", {})
        
        user_el = UI.get("element_labels", {}).get(dominant, dominant)
        idol_el = UI.get("element_labels", {}).get(idol_dominant, idol_dominant) if idol_dominant else user_el

        def f_str(s, idx=1, target=""):
            if not s: return ""
            # MZ 성향 키워드 추출
            u_mbti_trait = UI.get("mbti_trait_map", {}).get(user_mbti, "독창적인")
            
            # rel_type 지역화 (상생, 상극, 조화)
            s_labels = UI.get("SYNERGY_LABELS", {"생": "상생", "극": "상극", "조화": "조화"})
            raw_type = "생" if base_score > 70 else "극" if base_score < 40 else "조화"
            rel_type = s_labels.get(raw_type, s_labels.get("조화"))
            
            return s.format(
                user=display_user, idol=display_idol, n=idx, idx=idx,
                u_mbti=user_mbti, i_mbti=idol_mbti_fallback,
                mbti=user_mbti,
                u_el=user_el, i_el=idol_el,
                target=target,
                trait=_det_pick(f"{sampling_key}_trait_{idx}", UI.get("trait_map", {}).get(dominant, ["반전", "치명적"])),
                place=_det_pick(f"{sampling_key}_place_{idx}", UI.get("place_map", {}).get(dominant, ["단골", "추억의"])),
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
        
        # Map action guide keys to mission keys
        guide_map = {"vibe": "analysis_1", "heart": "analysis_2", "energy": "analysis_3"}
        
        used_combinations = set()
        for m_type, m_key in guide_map.items():
            idx = int(m_key.split('_')[1])
            m_seed_key = f"{sampling_key}_m{idx}"
            
            label_tpl = _det_pick(f"{m_seed_key}_lbl", m_labels)
            reason_tpl = _det_pick(f"{m_seed_key}_rsn", m_reasons)
            
            selected_tasks = []
            if is_gen:
                # 알고리즘 기반 파편화 생성 (1,000+ Variations)
                g_actions = mission_frags.get("actions", {}).get(mbti_e_i, mission_frags.get("actions", {}).get("I", []))
                g_targets = mission_frags.get("targets", {}).get(idol_dominant, mission_frags.get("targets", {}).get("Earth", []))
                g_contexts = mission_frags.get("contexts", ["시너지를 극대화하세요."])
                
                # 3개의 유니크한 조합 생성
                for t_idx in range(3):
                    attempt = 0
                    while True:
                        t_seed = f"{m_seed_key}_t{t_idx}_try{attempt}"
                        act = _det_pick(f"{t_seed}_a", g_actions)
                        tgt = _det_pick(f"{t_seed}_t", g_targets)
                        ctx = _det_pick(f"{t_seed}_c", g_contexts)
                        full_task = f"{act} {ctx}"
                        
                        # 체크 조합은 행동과 대상을 합쳐서 확인 (타겟이 달라져도 같은 행동이면 중복으로 처리)
                        # f_str 변환 후의 최종 완성 문장을 기준으로 중복 검사
                        final_sentence = f_str(full_task, idx, target=tgt)
                        
                        # 한국어 문법 호응 자동 교정 (어미와 서술어 맞춤)
                        # '만듭니다', '방법입니다', '길입니다', '마법입니다', '퍼즐입니다' -> 명사형 '하는 것은'
                        if any(x in final_sentence for x in ['방법입니다', '길입니다', '마법입니다', '퍼즐입니다', '만듭니다']):
                            final_sentence = final_sentence.replace('하며 ', '하는 것은 ').replace('갖으며 ', '갖는 것은 ').replace('쓰며 ', '쓰는 것은 ')
                        # '보세요', '하세요' -> 동시동작 '하며'
                        elif any(x in final_sentence for x in ['보세요', '하세요']):
                            final_sentence = final_sentence.replace('하는 것은 ', '하며 ').replace('갖는 것은 ', '갖으며 ').replace('쓰는 것은 ', '쓰며 ')
                            # Handle remaining edge cases caught by oracle
                            final_sentence = final_sentence.replace('남기는 것은', '남기며').replace('찍는 것은', '찍으며').replace('보태는 것은', '보태며')

                        # 단어 겹침 및 오타 최종 필터링
                        final_sentence = final_sentence.replace('매력 매력', '매력')
                        final_sentence = final_sentence.replace('공 성지순례', '공연장 성지순례').replace('원 성지순례', '응원 성지순례')
                        final_sentence = final_sentence.replace('감 매력', '반전 매력').replace('동 매력', '감동 매력').replace('생 매력', '생생한 매력')

                        if final_sentence not in used_combinations or attempt > 50:
                            used_combinations.add(final_sentence)
                            selected_tasks.append(final_sentence)
                            break
                        attempt += 1
            else:
                # 기존 방식 (폴백)
                tasks_pool = m_tasks_pool.get(m_type, ["{idx}번 미션 수행하기"])
                t_indices = list(range(len(tasks_pool)))
                random.seed(_hash_seed(f"{m_seed_key}_shuffle")) # 추가 시드 고정
                random.shuffle(t_indices)
                for t_idx in t_indices[:3]:
                    selected_tasks.append(f_str(tasks_pool[t_idx], idx))

            synergy_missions.append({
                "id": m_key,
                "label": f_str(label_tpl, idx),
                "boost": 15 if idx < 3 else 20,
                "reason": f_str(reason_tpl, idx),
                "tasks": selected_tasks,
                "completed": False
            })

        # Dynamic Tips Generation (1,000+ Combinations)
        tip_frags = loc.get("TIP_COMPONENTS", {})
        t_actions = tip_frags.get("actions", ["{mbti}답게"])
        t_topics = tip_frags.get("topics", ["{trait} 매력을"])
        t_results = tip_frags.get("results", ["성공하세요."])
        
        dynamic_tips = []
        for i in range(4):
            t_seed_key = f"{sampling_key}_tip{i}"
            act = _det_pick(f"{t_seed_key}_act", t_actions)
            top = _det_pick(f"{t_seed_key}_top", t_topics)
            res = _det_pick(f"{t_seed_key}_res", t_results)
            dynamic_tips.append(f_str(f"{act} {top} {res}", i+1))

        # 전문가 에이전트 피드백 (Health, Wealth, Career, Love)
        expert_seed = f"EXPERT_{sampling_key}"
        random.seed(_hash_seed(expert_seed))
        expert_advice = {}
        L_EXPERT_POOL = loc.get("EXPERT_ADVICE", {})
        
        for category, pool in L_EXPERT_POOL.items():
            if not pool: continue
            formatted_pool = []
            for advice in pool:
                adv = advice.format(
                    organ=UI.get("organ_map", {}).get(dominant, dominant),
                    body_part=UI.get("body_part_map", {}).get(dominant, dominant),
                    exercise=UI.get("exercise_map", {}).get(dominant, dominant),
                    month=random.randint(1, 12),
                    luck_item=UI.get("luck_item_map", {}).get(dominant, dominant),
                    star=UI.get("star_map", {}).get(dominant, dominant),
                    skill=UI.get("skill_map", {}).get(dominant, dominant),
                    element=UI.get("element_labels", {}).get(dominant, dominant),
                    trait=UI.get("trait_map", {}).get(dominant, dominant),
                    place=UI.get("place_map", {}).get(dominant, dominant)
                )
                formatted_pool.append(adv)
            expert_advice[category] = formatted_pool

        # 5인 전문가 에이전트 평생 사주
        L_LIFETIME_EXPERTS = loc.get("LIFETIME_EXPERTS", [])
        formatted_lifetime = []
        for exp in L_LIFETIME_EXPERTS:
            formatted_lifetime.append({
                "name": exp["name"],
                "focus": exp["focus"],
                "comment": exp["comment"].format(
                    season=UI.get("season_map", {}).get(dominant, dominant),
                    flower=UI.get("flower_map", {}).get(dominant, dominant),
                    industry=UI.get("industry_map", {}).get(dominant, dominant),
                    style=UI.get("style_map", {}).get(dominant, dominant),
                    mission=UI.get("mission_map", {}).get(dominant, dominant)
                )
            })

        # MZ Dynamic Analysis Synthesis (5-sentence logic)
        mz_report = assemble_mz_report(
            fragments, dominant, idol_dominant if idol_dominant else dominant, 
            user_mbti, idol_mbti, base_score, idol_name, lang, UI=UI,
            user_name=display_user
        )

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
            "synergy": synergy_text,
            "tips": dynamic_tips,
            "base_synergy_score": base_score,
            "synergy_missions": synergy_missions,
            "expert_advice": expert_advice,
            "lifetime_experts": formatted_lifetime
        }

        return {
            "dominant_element": dominant,
            "user_saju": user_saju,
            "monthly_fortune": monthly_fortune,
            "lifetime_fortune": lifetime_fortune,
            "chemistry_signal": chemistry_signal,
            "mz_saju_dictionary": loc.get("MZ_SAJU_DICTIONARY", {})
        }
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"Saju MZ Logic Error: {e}")
        return {"error": UI.get("error_msg", "Error in Saju Analysis.") if 'UI' in locals() else "Error in Saju Analysis."}
