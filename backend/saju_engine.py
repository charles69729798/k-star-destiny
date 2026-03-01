from typing import Dict, Any
import random
from datetime import datetime
from saju_i18n import get_localized_data, MBTI_CHEMISTRY

# ──────────────────────────────────────────────
# 1. K-사주 오행 별 심층 텍스트 베이스 (Soul Index) - KO Default
# ──────────────────────────────────────────────
# Note: All data constants (ENERGY_TRAITS, MONTH_DESCS, etc.) have been moved to saju_i18n.py

def get_element_relation(e1: str, e2: str) -> str:
    if e1 == e2: return "HARMONY"
    생_map = {"Wood":"Fire", "Fire":"Earth", "Earth":"Metal", "Metal":"Water", "Water":"Wood"}
    if 생_map.get(e1) == e2 or 생_map.get(e2) == e1: return "CREATE"
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

def _hash_seed(text: str) -> int:
    return sum(ord(c) for c in text)

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
    score_ranges = {"CREATE": (88, 98), "HARMONY": (82, 92), "CONTROL": (68, 85)}
    base_min, base_max = score_ranges.get(rel, (70, 90))
    
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

def assemble_mz_report(fragments: dict, user_el: str, idol_el: str, user_mbti: str, idol_mbti: str, score: int, idol_name: str, lang: str = "ko", UI: dict = None) -> dict:
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
    
    # 2. Bias Analysis (Essence + Point)
    essence = _det_pick(f"{base_key}_ess", fragments.get("bias_essence", [""])).format(element=idol_el)
    point = _det_pick(f"{base_key}_pt", fragments.get("bias_point", [""]))
    bias_desc = f"{essence} {point}"
    
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
        mbti=idol_mbti, mbti_trait=trait_desc
    )
    
    # 4. Recent Fortune — 결정론적 선택 (KO와 동일 인덱스 → 의미 일치)
    recent = _det_pick(f"{base_key}_fortune", fragments.get("recent_fortune", ["오늘도 빛나는 하루!"])).format(idol=idol_name)
    
    # 5. Synergy Why
    synergy_why = _det_pick(f"{base_key}_why", fragments.get("synergy_why", [""])).format(
        u_element=user_el, i_element=idol_el, u_mbti=user_mbti, i_mbti=idol_mbti
    )
    
    return {
        "relationship": relationship,
        "bias": bias_desc,
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
                "guide": guide,
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
        
        def f_str(s):
            if not s: return ""
            # Context Override based on Score & Element Relationship
            if base_score < 60:
                s = s.replace("[도파민 폭발]", "[에너지 회복]").replace("[Dopamine Explosion]", "[Energy Recovery]").replace("[Explosión de Dopamina]", "[Recuperación de Energía]").replace("[Explosão de Dopamina]", "[Recuperação de Energía]")
                s = s.replace("하이텐션 듀오", "케미 복구 듀오").replace("High Tension Duo", "Chemistry Recovery Duo").replace("Dúo de Alta Tensión", "Dúo de Recuperación de Química").replace("Dupla de Alta Tensão", "Dupla de Recuperação de Química")
            
            return s.format(user=display_user, idol=display_idol)

        synergy_missions = []
        if isinstance(missions_raw, dict):
            # Dynamic Content Generation for Missions
            # Using fragments to create labels and reasons
            points = [
                f"{dominant} vs {idol_dominant or dominant} 에너지 차이" if lang == "ko" else f"Energy Gap: {dominant} vs {idol_dominant or dominant}",
                f"{user_mbti} & {idol_mbti} 소통 방식" if lang == "ko" else f"Talk Vibe: {user_mbti} & {idol_mbti}",
                "우주적 시너 솔루션" if lang == "ko" else "Cosmic Synergy Solution"
            ]
            reasons = [
                f"서로의 {dominant}/{idol_dominant or dominant} 성향이 만나 생기는 자기장" if lang == "ko" else f"Magnetic field from {dominant}/{idol_dominant or dominant} elements",
                f"{user_mbti}의 {user_mbti[2:] if user_mbti and len(user_mbti)>2 else user_mbti}와 {idol_mbti}의 {idol_mbti[2:] if idol_mbti and len(idol_mbti)>2 else idol_mbti} 성향 차이" if lang == "ko" else f"Traits diff between {user_mbti} and {idol_mbti}",
                "운명적인 주파수 동기화" if lang == "ko" else "Destined frequency sync"
            ]
            
            # Map action guide keys to mission keys
            guide_map = {"vibe": "analysis_1", "heart": "analysis_2", "energy": "analysis_3"}
            action_guides_mz = fragments.get("action_guides", {})
            
            for m_key, guide_key in guide_map.items():
                m_data = missions_raw.get(guide_key, {})
                if not m_data: continue
                
                idx = int(guide_key.split('_')[1]) - 1
                point_val = points[idx]
                reason_val = reasons[idx]
                
                # Get tasks from action guides if available
                guide_pool = action_guides_mz.get(m_key, [])
                if len(guide_pool) >= 3:
                    tasks = random.sample(guide_pool, 3)
                elif len(guide_pool) > 0:
                    # 가이드가 3개 미만이면 기존 가이드를 순환 재사용하여 3개를 채움
                    tasks = [guide_pool[i % len(guide_pool)] for i in range(3)]
                else:
                    # action_guides 데이터가 아예 없으면 빈 리스트 (UI에서 빈 칸으로 표시)
                    tasks = []
                
                label = m_data.get("label", "").format(point_1=point_val, point_2=point_val, point_3=point_val)
                reason = m_data.get("reason", "").format(reason_1=reason_val, reason_2=reason_val, reason_3=reason_val)
                
                # {idol} 플레이스홀더를 실제 아이돌 이름으로 치환
                def _fmt_task(t: str) -> str:
                    try:
                        return f_str(t.format(idol=idol_name))
                    except Exception:
                        return f_str(t)
                
                synergy_missions.append({
                    "id": guide_key,
                    "boost": m_data.get("boost", 15),
                    "label": f_str(label),
                    "reason": f_str(reason),
                    "tasks": [_fmt_task(t) for t in tasks],
                    "completed": False
                })

        # 전문가 에이전트 피드백 (Health, Wealth, Career, Love)
        # BUG FIX: Seed must include idol info to be unique per partner
        expert_seed = f"EXPERT_{user_seed}_{idol_name}_{idol_birth_date}"
        random.seed(_hash_seed(expert_seed))
        expert_advice = {}
        L_EXPERT_POOL = loc.get("EXPERT_ADVICE", {})
        
        # Mapping elements to organs/categories
        organ_map = {"Wood": "간/담", "Fire": "심장/소장", "Earth": "위/비장", "Metal": "폐/대장", "Water": "신장/방광"}
        body_part_map = {"Wood": "근육/눈", "Fire": "혈관/혀", "Earth": "피부/입", "Metal": "호흡기/코", "Water": "뼈/귀"}
        exercise_map = {"Wood": "산책/필라테스", "Fire": "고강도 인터벌/댄스", "Earth": "등산/근력운동", "Metal": "요가/복싱", "Water": "수영/명상"}
        
        for category, pool in L_EXPERT_POOL.items():
            if not pool: continue
            # 필드 치환 (예: {organ}, {exercise} 등)
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

        # 5인 전문가 에이전트 평생 사주 (LIFETIME_EXPERTS)
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
            fragments, 
            dominant, 
            idol_dominant if idol_dominant else dominant, 
            user_mbti, 
            idol_mbti, 
            base_score, 
            display_idol, 
            lang,
            UI=UI
        )

        # Enhance missions with specific action guides if present
        action_guides = mz_report.get("actionGuides", {})
        if synergy_missions and action_guides:
            for mission in synergy_missions:
                m_cat = mission["id"].replace("mission_", "") # e.g., vibe, heart, energy
                if m_cat in action_guides:
                    guide_pool = action_guides[m_cat]
                    # Select 2 action tasks if they are not already in tasks
                    action_tasks = random.sample(guide_pool, min(2, len(guide_pool)))
                    # Merge with existing tasks (ensure unique and max 3 total)
                    mission["tasks"] = list(dict.fromkeys(mission["tasks"] + action_tasks))[:3]
                    mission["action_guide"] = random.choice(guide_pool)

        chemistry_signal = {
            "idol_name": display_idol,
            "idol_mbti": idol_mbti_fallback,
            "idol_birth_date": idol_birth_date,
            "idol_detailed_traits": [mz_report["bias"]],
            "relationship": mz_report["relationship"],
            "bias": mz_report["bias"],
            "tmi": mz_report["tmi"],
            "recentFortune": mz_report["recentFortune"],
            "synergyWhy": mz_report["synergyWhy"],
            "synergy": synergy_text,
            "tips": [f_str(t) for t in random.sample(L_CUR_TIPS, min(4, len(L_CUR_TIPS)))] if L_CUR_TIPS else [],
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
