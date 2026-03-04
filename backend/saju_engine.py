from typing import Dict, Any
import random
import re
from datetime import datetime
from saju_i18n import get_localized_data, CONTEXT_MAPS, I18N_DATA
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
    pattern = re.compile("|".join(re.escape(k) for k in sorted_keys))
    return pattern.sub(lambda m: context_map[m.group(0)], text)


def get_element_relation(e1: str, e2: str) -> str:
    if e1 == e2:
        return "HARMONY"
    if ELEMENT_CREATION_MAP.get(e1) == e2 or ELEMENT_CREATION_MAP.get(e2) == e1:
        return "CREATE"
    return "CONTROL"


def get_mbti_quad_description(mbti: str, lang: str = "ko") -> list:
    """MBTI 4개 기능을 조합하여 분자 수준의 성격 묘사를 생성합니다."""
    loc = get_localized_data(lang)
    UI = loc.get("UI_STRINGS", {})

    # MBTI 정보가 없을 경우 오행 기반 기본 묘사 반환
    if not mbti or len(mbti) != 4:
        return [
            UI.get("mbti_unknown_desc", "신비로운 잠재력을 지닌 에너지가 느껴집니다.")
        ]

    mbti_fragments = loc.get("MBTI_FUNC_FRAGMENTS", {})
    if not mbti_fragments:
        return []

    m = mbti.upper()
    descriptions = []

    # E/I, N/S, T/F, J/P 순서로 조립
    mapping = [("e_i", 0), ("n_s", 1), ("t_f", 2), ("j_p", 3)]
    for key, idx in mapping:
        fragment = mbti_fragments.get(key, {}).get(m[idx], "")
        if fragment:
            descriptions.append(fragment)

    return descriptions


def generate_scientific_hypothesis(
    weights: Dict[str, int], mbti: str, lang: str = "ko", is_user: bool = False
) -> str:
    """오행 가중치와 MBTI를 결합하여 정밀 가설을 생성합니다 (RPRE 엔진)."""
    if not weights or not mbti:
        return ""

    loc = get_localized_data(lang)
    UI = loc.get("UI_STRINGS", {})

    # MBTI가 없는 경우 기본값 할당 (분석 누락 방지)
    mbti_val = mbti if mbti else UI.get("mbti_unrevealed", "Secret")

    rpre_key = "RPRE_TEMPLATES_USER" if is_user else "RPRE_TEMPLATES"
    rpre_data = loc.get(rpre_key, loc.get("RPRE_TEMPLATES", {}))
    if not rpre_data:
        return ""

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
        # YYYY-MM-DD 형식을 엄격하게 검증 (불완전한 연도만 있는 경우 등 차단)
        if not re.match(r"^\d{4}-\d{2}-\d{2}", date_str):
            raise ValueError(f"Invalid date format: {date_str}. Expected YYYY-MM-DD")
        d = datetime.strptime(date_str[:10], "%Y-%m-%d")
    except Exception as e:
        # 에러 발생 시 더 이상 기본값(20% 균등배분)을 반환하지 않고 예외를 상위로 전파
        raise ValueError(f"Saju calculation failed: Invalid birth date '{date_str}'.") from e

    sc = {el: 10 for el in elements}  # 기본값 (보정)

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


def generate_monthly_fortune(
    keywords, descs, seed_val: str = None, month_names: list = None
) -> list:
    if seed_val:
        random.seed(_hash_seed(seed_val))

    monthly = []

    if not keywords or not descs:
        return []

    # We now have exactly 12 items for each to ensure sequence integrity
    for i in range(12):
        k = keywords[i] if i < len(keywords) else keywords[-1]

        # Enhanced Randomness: Handle expanded flat list by using seed-based offset
        if (
            isinstance(descs, list)
            and len(descs) > 12
            and not isinstance(descs[0], list)
        ):
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
            m_str = str(i + 1)

        monthly.append({"month": m_str, "keyword": k, "desc": d})

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
        s.get("senior", ""),
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
    except:
        pass

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

    if not missions:
        return []

    tag_map = {
        "Fire": [
            "[Viral]",
            "[Challenge]",
            "[Party]",
            "[Cafe]",
            "[Karaoke]",
            "[Adrenaline]",
            "[Passion]",
            "[Rhythm]",
            "[Busking]",
        ],
        "Water": [
            "[Chill]",
            "[Zen]",
            "[Bookworm]",
            "[Secret]",
            "[Quiet]",
            "[Lake]",
            "[Aquarium]",
            "[Meditation]",
            "[Disconnect]",
        ],
        "Earth": [
            "[Foodie]",
            "[Nature]",
            "[Camping]",
            "[Zoo]",
            "[Garden]",
            "[Bakery]",
            "[Picnic]",
            "[Street Food]",
            "[Market]",
        ],
        "Wood": [
            "[Growth]",
            "[Grind]",
            "[Aesthetic]",
            "[Style]",
            "[Vlog]",
            "[Glow-up]",
            "[Photography]",
            "[Custom]",
            "[4-cut]",
            "[Fashion]",
        ],
        "Metal": [
            "[Luxury]",
            "[Art]",
            "[Tech]",
            "[Museum]",
            "[History]",
            "[Gallery]",
            "[Castle]",
            "[Modern Art]",
            "[Architecture]",
        ],
    }

    preferred_tags = tag_map.get(element, [])
    # Filter missions that have at least one preferred tag
    filtered = [m for m in missions if any(tag in str(m) for tag in preferred_tags)]

    # If not enough filtered missions, use original set
    source = filtered if len(filtered) >= 3 else missions
    selected = random.sample(source, min(3, len(source)))

    return selected


def assemble_mz_report(
    fragments: dict,
    user_el: str,
    idol_el: str,
    user_mbti: str,
    idol_mbti: str,
    score: int,
    idol_name: str,
    lang: str = "ko",
    UI: dict = None,
    user_name: str = "You",
    is_friend: bool = False,
    partner_word: str = "스타",
) -> dict:
    """하드코딩 배제: 조각들을 조합하여 5문장 이상의 디테일한 MZ 리포트 생성
    ✅ 언어에 관계없이 동일한 내용(인덱스)이 선택되도록 _det_pick() 사용"""
    # 결정론적 시드 키 (언어 제외 → 언어마다 같은 항목 선택)
    base_key = (
        f"MZ_REPORT_D5_{user_el}_{idol_el}_{user_mbti}_{idol_mbti}_{score}_{idol_name}"
    )

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
    essence = _det_pick(f"{base_key}_ess", fragments.get("bias_essence", [""])).format(
        element=idol_el
    )
    point = _det_pick(f"{base_key}_pt", fragments.get("bias_point", [""]))
    growth = _det_pick(f"{base_key}_growth", fragments.get("bias_growth", [""]))
    aura = _det_pick(f"{base_key}_aura", fragments.get("bias_aura", [""]))

    # 3. MBTI TMI
    mbti_traits = UI.get("MBTI_TRAITS", {})
    trait_desc = mbti_traits.get(
        idol_mbti[0].upper() if idol_mbti and idol_mbti != "Unknown" else "E",
        UI.get("mysterious_label", "신비로운"),
    )
    bias_tmi = _det_pick(f"{base_key}_tmi", fragments.get("bias_tmi", [""])).format(
        mbti=idol_mbti,
        mbti_trait=trait_desc,
        user=user_name,
        idol=idol_name,
        u_el=user_el,
        i_el=idol_el,
        u_mbti=user_mbti,
        i_mbti=idol_mbti,
    )

    # Combined Bias Description (5 sentences)
    bias_desc = f"{essence} {point} {growth} {aura} {bias_tmi}"

    # 4. Recent Fortune (이제 미션 섹션의 상단 동기부여 '명분'으로 활용됨)
    recent = _det_pick(
        f"{base_key}_fortune",
        fragments.get(
            "recent_fortune", [UI.get("default_fortune_msg", "빛나는 하루!")]
        ),
    ).format(
        idol=idol_name,
        user=user_name,
        u_el=user_el,
        i_el=idol_el,
        u_mbti=user_mbti,
        i_mbti=idol_mbti,
    )

    # 5. Synergy Why
    synergy_why = _det_pick(
        f"{base_key}_why", fragments.get("synergy_why", [""])
    ).format(
        u_element=user_el,
        i_element=idol_el,
        u_mbti=user_mbti,
        i_mbti=idol_mbti,
        user=user_name,
        idol=idol_name,
        u_el=user_el,
        i_el=idol_el,
    )

    # [MZ UX 고도화] 최근 운세 정보를 미션 섹션의 'Context'로 최상단 배치하도록 유도
    scan_label = (
        UI.get("aura_scan_label", "Aura Scan")
        if not is_friend
        else UI.get("friend_scan_label", "Friend Scan")
    )
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
        "actionGuides": fragments.get("action_guides", {}),
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
            for field in [
                "relationship",
                "bias",
                "tmi",
                "recentFortune",
                "synergyWhy",
                "missionMotivation",
            ]:
                if field in report_dict:
                    report_dict[field] = report_dict[field].replace(k, v)

            # 리스트 필드 치환
            report_dict["bias_list"] = [
                item.replace(k, v) for item in report_dict["bias_list"]
            ]

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
# Helper Functions for Analysis Synthesis
# ──────────────────────────────────────────────


def _get_user_saju(dominant, user_weights, user_mbti, lang, UI) -> dict:
    user_mbti_logic = get_mbti_quad_description(user_mbti, lang)
    user_rpre = generate_scientific_hypothesis(
        user_weights, user_mbti, lang, is_user=True
    )

    mbti_e_i = "default"
    if user_mbti and len(user_mbti) > 0 and user_mbti.upper()[0] in ["E", "I"]:
        mbti_e_i = user_mbti.upper()[0]

    display_user = UI.get("user_name_fallback", "You")
    loc = get_localized_data(lang)
    L_ENERGY_TRAITS = loc.get("ENERGY_TRAITS", {})
    trait = L_ENERGY_TRAITS.get(dominant, L_ENERGY_TRAITS.get("Earth"))

    c_intro_raw = (
        random.choice(trait.get("desc_intro", [""]))
        if isinstance(trait.get("desc_intro"), list)
        else trait.get("desc_intro", "")
    )
    c_intro = c_intro_raw.format(user=display_user)

    mbti_core = " ".join(user_mbti_logic) if user_mbti_logic else ""
    c_core_pool = trait.get("desc_core", {}).get(
        mbti_e_i, trait.get("desc_core", {}).get("default", [""])
    )
    if not c_core_pool or isinstance(c_core_pool, str):
        c_core_pool = [c_core_pool]
    c_core_raw = random.choice(c_core_pool)
    c_core = c_core_raw.format(user=display_user)

    c_advice_raw = (
        random.choice(trait.get("desc_advice", [""]))
        if isinstance(trait.get("desc_advice"), list)
        else trait.get("desc_advice", "")
    )
    c_advice = c_advice_raw.format(user=display_user)

    weight_summary = ", ".join(
        [
            f"{UI.get('element_labels', {}).get(k, k)} {v}%"
            for k, v in user_weights.items()
            if v > 10
        ]
    )

    user_saju_content = (
        f"📊 {UI.get('scientific_analysis', 'Scientific Analysis')}\n"
        f"- {UI.get('element_weight', 'Element Weights')}: {weight_summary}\n"
        f"- {UI.get('mbti_dynamic', 'MBTI Dynamics')}: {mbti_core}\n\n"
        f"🔬 {UI.get('rpre_hypothesis', 'Persona Hypothesis')}\n{user_rpre}\n\n"
        f"✨ {UI.get('signature', 'Signature')}\n{c_intro}\n\n"
        f"💡 {UI.get('potential', 'Potential')}\n{c_core}\n\n"
        f"🚀 {UI.get('guide', 'Guide')}\n{c_advice}"
    )

    return {
        "summary": trait["name"],
        "element": dominant,
        "elements": user_weights,
        "content": user_saju_content,
    }


def _get_monthly_fortune(
    user_seed,
    display_idol,
    display_user,
    el_text,
    user_el,
    idol_el,
    is_friend,
    partner_word,
    lang,
    loc,
) -> list:
    monthly_fortune = []
    L_MONTH_FORTUNES = loc.get("MONTH_FORTUNES", {})

    from saju_i18n import CONTEXT_MAPS

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

    def render_and_replace(tpl):
        if not tpl:
            return ""
        try:
            out = tpl.format(
                idol=display_idol,
                user=display_user,
                dominant=el_text,
                u_el=user_el,
                i_el=idol_el,
            )
        except (KeyError, IndexError):
            out = tpl

        if is_friend:
            for k in sorted_keys:
                out = out.replace(k, final_context[k])
        return out

    for m in range(1, 13):
        m_str = str(m)
        m_data = L_MONTH_FORTUNES.get(m_str, {})
        m_seed = f"{user_seed}_MONTH_{m}"
        random.seed(_hash_seed(m_seed))
        m_score = random.randint(60, 95)

        raw_theme = m_data.get("theme", "")
        raw_signal = m_data.get("signal", "")
        raw_guide = m_data.get("guide", m_data.get("action_point", ""))

        theme_rendered = render_and_replace(raw_theme)
        star_signal = render_and_replace(raw_signal)
        action_point = render_and_replace(raw_guide)

        monthly_fortune.append(
            {
                "month": m,
                "theme": theme_rendered,
                "signal": star_signal,
                "star_signal": star_signal,
                "guide": action_point,
                "action_point": action_point,
                "score": m_score,
                "synergy": m_score,
            }
        )
    return monthly_fortune


def _generate_dynamic_tips(user_saju, target_saju, u_mbti, i_mbti, lang, is_friend, seed_val, loc):
    """
    Generates 3 dynamic success tips by combining fragments based on Saju/MBTI.
    """
    import random
    rng = random.Random(seed_val)
    
    comps = loc.get("TIP_COMPONENTS", {})
    if not comps:
        return []
        
    # Define {target} based on mode
    target_label = "친구" if is_friend else "스타"
    if lang == 'en': target_label = "friend" if is_friend else "star"
    elif lang == 'es': target_label = "amigo/a" if is_friend else "estrella"
    elif lang == 'pt': target_label = "amigo(a)" if is_friend else "idol"
    
    # Context variable map for f_str
    u_el = user_saju.get('dominant_element', '목')
    i_el = target_saju.get('dominant_element', '목')
    mbti = i_mbti if i_mbti else "???"
    mbti_trait = i_mbti[0] if i_mbti and len(i_mbti)>0 else "E"
    
    actions = list(comps.get('actions', []))
    topics = list(comps.get('topics', []))
    results = list(comps.get('results', []))
    
    rng.shuffle(actions)
    rng.shuffle(topics)
    rng.shuffle(results)
    
    UI = loc.get("UI_STRINGS", {})
    u_dom_en = user_saju.get('dominant_en', 'Wood')
    el_idx_map = {"Wood": 0, "Fire": 1, "Earth": 2, "Metal": 3, "Water": 4}
    idx_v = el_idx_map.get(u_dom_en, 0)
    
    def get_mapped(key, default):
        pool = UI.get(key, [default])
        if isinstance(pool, list):
            return pool[idx_v] if len(pool) > idx_v else default
        if isinstance(pool, dict):
            return pool.get(u_dom_en, default)
        return default

    rel_type = UI.get("SYNERGY_LABELS", {}).get("조화", "조화")
    
    context_vars = {
        'target': target_label,
        'u_el': u_el,
        'i_el': i_el,
        'mbti': mbti,
        'mbti_trait': mbti_trait,
        'u_mbti': u_mbti,
        'trait': get_mapped("trait_map", "매력"),
        'place': get_mapped("place_map", "장소"),
        'organ': get_mapped("health_focus", "건강"),
        'star': get_mapped("star_map", "성향"),
        'luck_item': get_mapped("luck_item_map", "행운템"),
        'skill': get_mapped("skill_map", "재능"),
        'exercise': get_mapped("exercise_map", "운동"),
        'rel_type': rel_type,
        'star_word': UI.get("star_word", "스타")
    }
    
    tips = []
    # Pick 3 unique combinations
    for i in range(min(3, len(actions), len(topics), len(results))):
        if i % 2 == 0:
            raw_tip = f"{actions[i]} {topics[i]} {results[i]}"
        else:
            raw_tip = f"{topics[i]} {actions[i]} {results[i]}"
            
        try:
            # Simple format replacement
            resolved_tip = raw_tip.format(**context_vars)
            
            # Post-processing for Korean natural text (은/는, 이/가 등)
            if lang == "ko":
                resolved_tip = resolved_tip.replace("  ", " ")
                
            tips.append(resolved_tip)
        except Exception as e:
            print(f"Error resolving tip: {raw_tip}, error: {e}")
            
    return tips


def _get_synergy_missions(
    dominant,
    idol_dominant,
    birth_date_str,
    idol_birth_date,
    user_mbti,
    idol_mbti,
    user_seed,
    idol_name,
    partner_word,
    lang,
    loc,
    UI,
    is_friend,
    is_gen,
    base_score,
    display_user,
    display_idol,
    idol_mbti_fallback,
    user_el,
    idol_el,
) -> list:
    sh_seed = f"SHUFFLE_{user_seed}_{idol_name}"
    sampling_key = (
        f"MISSION_{user_seed}_{dominant}_{user_mbti}_{idol_name}_{base_score}"
    )

    mbti_e_i = "default"
    if user_mbti and len(user_mbti) > 0 and user_mbti.upper()[0] in ["E", "I"]:
        mbti_e_i = user_mbti.upper()[0]

    def f_str(s, idx=1, target=""):
        if not s:
            return ""

        el_idx_map = {"Wood": 0, "Fire": 1, "Earth": 2, "Metal": 3, "Water": 4}
        idx_v = el_idx_map.get(dominant, 0)
        u_mbti_trait = UI.get("mbti_trait_map", {}).get(user_mbti, "독창적인")
        s_labels = UI.get(
            "SYNERGY_LABELS", {"생": "상생", "극": "상극", "조화": "조화"}
        )
        raw_type = "생" if base_score > 70 else "극" if base_score < 40 else "조화"
        rel_type = s_labels.get(raw_type, s_labels.get("조화"))

        trait_pool = UI.get("trait_map", ["매력"])
        place_pool = UI.get("place_map", ["장소"])
        cur_trait = (
            trait_pool[idx_v]
            if isinstance(trait_pool, list)
            else trait_pool.get(dominant, "매력")
        )
        cur_place = (
            place_pool[idx_v]
            if isinstance(place_pool, list)
            else place_pool.get(dominant, "장소")
        )

        i_group = UI.get("star_word", "아이돌") if not is_friend else partner_word
        if not is_friend and idol_name:
            parts = display_idol.split()
            i_group = parts[0] if len(parts) > 1 else display_idol

        try:
            formatted_text = s.format(
                user=display_user,
                idol=display_idol,
                n=idx,
                idx=idx,
                u_mbti=user_mbti if user_mbti else UI.get("mbti_unrevealed", "Secret"),
                i_mbti=(
                    idol_mbti_fallback
                    if idol_mbti_fallback
                    else UI.get("mbti_unrevealed", "Secret")
                ),
                mbti=user_mbti if user_mbti else UI.get("mbti_unrevealed", "Secret"),
                u_el=user_el,
                i_el=idol_el,
                target=target,
                idol_group=i_group,
                i_group=i_group,
                trait=cur_trait,
                place=cur_place,
                organ=UI.get("organ_map", {}).get(dominant, "에너지"),
                luck_item=UI.get("luck_item_map", {}).get(dominant, "아이템"),
                star=UI.get("star_map", {}).get(dominant, "별자리"),
                skill=UI.get("skill_map", {}).get(dominant, "능력"),
                mbti_trait=u_mbti_trait,
                rel_type=rel_type,
                point=_det_pick(
                    f"{sampling_key}_pt_{idx}", UI.get("MISSION_POINTS", ["특별한"])
                ),
                exercise=UI.get("exercise_map", {}).get(dominant, "운동"),
            )
            
            if is_friend:
                from saju_i18n import CONTEXT_MAPS

                lang_context = CONTEXT_MAPS.get(lang, CONTEXT_MAPS.get("ko", {}))
                final_context = lang_context.copy()
                if lang == "ko":
                    final_context.update(
                        {
                            "스타": partner_word,
                            "스타가": f"{partner_word}가",
                            "스타는": f"{partner_word}는",
                            "스타를": f"{partner_word}를",
                            "스타의": f"{partner_word}의",
                            "스타와": f"{partner_word}와",
                        }
                    )
                formatted_text = context_aware_replace(formatted_text, final_context)
            
            return formatted_text
        except:
            return s

    synergy_missions = []
    mission_frags = loc.get("GEN_MISSION_COMPONENTS", loc.get("MISSION_COMPONENTS", {}))
    m_labels = mission_frags.get("labels", ["Analysis {n}"])
    m_reasons = mission_frags.get("reasons", ["Due to {u_el} & {i_el} synergy"])
    guide_map = {"vibe": "analysis_1", "heart": "analysis_2", "energy": "analysis_3"}

    # ── 오행 관계 판별 (상생/상극/동기) ──────────────────────────
    from saju_rules import ELEMENT_CREATION_MAP
    _el_creation = ELEMENT_CREATION_MAP  # {생: [...], 극: [...]}
    el_pair = (dominant, idol_dominant if idol_dominant else dominant)
    # 상생인지 확인: A가 B를 생하거나 B가 A를 생하면 상생
    creation_pairs = _el_creation if isinstance(_el_creation, dict) else {}
    def is_creation(a, b):
        for src, targets in creation_pairs.items():
            if src == a and b in (targets if isinstance(targets, list) else [targets]):
                return True
        return False
    is_same_el = el_pair[0] == el_pair[1]
    is_gen_rel = is_creation(el_pair[0], el_pair[1]) or is_creation(el_pair[1], el_pair[0])
    
    def _get_ctx_pool_by_rel(g_contexts):
        """오행 관계에 따라 적절한 context 풀 반환"""
        if not g_contexts:
            return ["함께하는 특별한 시간이에요."]
        if is_gen_rel:
            oehaeng_ctxs = [c for c in g_contexts if "{i_el}" in c or "{u_el}" in c]
            if oehaeng_ctxs:
                return oehaeng_ctxs
        if is_same_el:
            deep_ctxs = [c for c in g_contexts if "깊" in c or "알아" in c or "이해" in c]
            if deep_ctxs:
                return deep_ctxs
        return g_contexts

    if is_gen:
        all_actions = mission_frags.get("actions", {})
        u_mbti_upper = (user_mbti or "").upper().strip()
        
        # ── MBTI 16기질 액션 풀이 5개 수준이므로, E/I 범용 풀과 병합하여 최소 10~15개 보장 ──
        mbti_spec = all_actions.get(u_mbti_upper, [])
        fb_ei = all_actions.get(mbti_e_i, [])
        fb_mode = all_actions.get("E" if is_friend else "I", [])
        
        merged_actions = mbti_spec + [x for x in fb_ei if x not in mbti_spec]
        merged_actions = merged_actions + [x for x in fb_mode if x not in merged_actions]
        g_actions = merged_actions if merged_actions else ["함께 시간을 보내며", "서로의 이야기를 들으며"]

        # ── 스타/지인별 전용 타겟 풀 선택 로직 추가 ──
        target_pool_key = "targets_friend" if is_friend else "targets"
        g_targets_pool = mission_frags.get(target_pool_key, mission_frags.get("targets", {}))
        g_targets = g_targets_pool.get(
            idol_dominant if idol_dominant else dominant,
            g_targets_pool.get("Earth", ["특별한 아이템", "새로운 장소"]),
        )
        
        g_contexts = mission_frags.get("contexts", ["시너지를 극대화하세요."])

        sh_seed_gen = f"GEN_SHUFFLE_{user_seed}_{idol_name}"
        m_labels_gen = m_labels.copy()
        m_reasons_gen = m_reasons.copy()
        
        # idol_name이 포함된 sh_seed_gen을 사용하여 동일 유저라도 스타마다 다른 카드가 나오도록 보장
        random.seed(_hash_seed(sh_seed_gen))
        random.shuffle(m_labels_gen)
        random.shuffle(m_reasons_gen)
        
        # 반복(중복)을 최소화하기 위해 리스트 셔플 후 순환 참조 (풀 크기 최소 9 이상 보장)
        uniq_actions = random.sample(g_actions, min(9, len(g_actions)))
        
        ctx_pool = _get_ctx_pool_by_rel(g_contexts)
        uniq_contexts = random.sample(ctx_pool, min(9, len(ctx_pool))) if ctx_pool else ["최고의 순간을 만드세요."]
        
        uniq_targets = random.sample(g_targets, min(9, len(g_targets)))

        combo_idx = 0
        for m_type, m_key in guide_map.items():
            idx = int(m_key.split("_")[1])
            m_seed_key = f"{sampling_key}_m{idx}"
            label_tpl = m_labels_gen.pop() if m_labels_gen else f"Mission {idx}"
            reason_tpl = m_reasons_gen.pop() if m_reasons_gen else "Destiny choice"

            selected_tasks_detailed = []
            for _ in range(3):
                act = uniq_actions[combo_idx % len(uniq_actions)]
                tgt = uniq_targets[combo_idx % len(uniq_targets)]
                ctx = uniq_contexts[combo_idx % len(uniq_contexts)]
                combo_idx += 1

                final_sentence = f_str(f"{act} {ctx}", idx, target=tgt)

                if lang == "ko":
                    if any(
                        x in final_sentence
                        for x in [
                            "방법입니다",
                            "길입니다",
                            "마법입니다",
                            "퍼졸입니다",
                            "만듭니다",
                            "치트키입니다",
                            "루틴입니다",
                            "비결입니다",
                        ]
                    ):
                        final_sentence = (
                            final_sentence.replace("하며 ", "하는 것은 ")
                            .replace("갖으며 ", "갖는 것은 ")
                            .replace("쓰며 ", "쓰는 것은 ")
                            .replace("보내며", "보내는 것은")
                            .replace("때리며", "때리는 것은")
                            .replace("매며", "매는 것은")
                        )
                    elif any(x in final_sentence for x in ["보세요", "하세요"]):
                        final_sentence = (
                            final_sentence.replace("하는 것은 ", "하며 ")
                            .replace("갖는 것은 ", "갖으며 ")
                            .replace("쓰는 것은 ", "쓰며 ")
                            .replace("보내는 것은", "보내며")
                            .replace("때리는 것은", "때리며")
                            .replace("매는 것은", "매며")
                        )

                candidates = [
                    w.strip("!?,.") for w in final_sentence.split() if len(w) >= 2
                ]
                kw = (
                    candidates[1]
                    if len(candidates) > 1
                    else candidates[0][:3] if candidates else "미션"
                )

                selected_tasks_detailed.append(
                    {"task": final_sentence.replace("  ", " "), "keyword": kw}
                )
                combo_idx += 1

            synergy_missions.append(
                {
                    "id": m_key,
                    "label": f_str(label_tpl, idx),
                    "boost": 15 if idx < 3 else 20,
                    "reason": f_str(reason_tpl, idx),
                    "tasks": [t["task"] for t in selected_tasks_detailed],
                    "tasks_detailed": selected_tasks_detailed,
                    "completed": False,
                }
            )
    else:
        # Fallback (Original Multi-lang Logic)
        m_comp_key = (
            "GEN_MISSION_COMPONENTS_FRIEND" if is_friend else "GEN_MISSION_COMPONENTS"
        )
        mission_frags_sp = loc.get(
            m_comp_key,
            loc.get("GEN_MISSION_COMPONENTS", loc.get("MISSION_COMPONENTS", {})),
        )
        m_labels_sp = mission_frags_sp.get("labels", ["Mission"]).copy()
        m_reasons_sp = mission_frags_sp.get("reasons", ["Analysis result"]).copy()
        m_tasks_map_sp = mission_frags_sp.get("tasks", {})

        random.seed(_hash_seed(sh_seed))
        random.shuffle(m_labels_sp)
        random.shuffle(m_reasons_sp)

        SUPPORT_LANGS = ["ko", "en", "es", "pt"]
        for i in range(1, 4):
            mission_item = {"id": i, "boost": 15 if i < 3 else 20}
            for l in SUPPORT_LANGS:
                l_loc = I18N_DATA.get(l, I18N_DATA["en"])
                l_UI = l_loc.get("UI_STRINGS", {})
                l_frags = l_loc.get(
                    m_comp_key if is_friend else "GEN_MISSION_COMPONENTS",
                    l_loc.get("MISSION_COMPONENTS", {}),
                )
                l_labels = l_frags.get("labels", ["Mission"]).copy()
                l_reasons = l_frags.get("reasons", ["Result"]).copy()
                l_tasks_map = l_frags.get("tasks", {})

                random.seed(_hash_seed(f"{sh_seed}_LBL_{i}"))
                label_tpl = (
                    l_labels[random.randint(0, len(l_labels) - 1)]
                    if l_labels
                    else f"Mission {i}"
                )
                random.seed(_hash_seed(f"{sh_seed}_RSN_{i}"))
                reason_tpl = (
                    l_reasons[random.randint(0, len(l_reasons) - 1)]
                    if l_reasons
                    else "Result"
                )

                cat = ["vibe", "heart", "energy"][i - 1]
                # 스타 모드와 지인 모드의 미션 풀 완전 분리
                if is_friend:
                    task_pool = l_tasks_map.get("friend_tasks", {}).get(cat, l_tasks_map.get(cat, [f"Challenge {i}"]))
                else:
                    task_pool = l_tasks_map.get("star_tasks", {}).get(cat, l_tasks_map.get(cat, [f"Challenge {i}"]))

                l_tasks_raw = []
                for idx_seq in range(3):
                    random.seed(_hash_seed(f"{sh_seed}_TSK_{i}_{idx_seq}"))
                    t_idx = random.randint(0, len(task_pool) - 1) if task_pool else 0
                    l_tasks_raw.append(f_str(task_pool[t_idx], i))

                suffix = "" if l == lang else f"_{l}"
                mission_item[f"label{suffix}"] = f_str(label_tpl, i)
                mission_item[f"reason{suffix}"] = f_str(reason_tpl, i)
                mission_item[f"tasks{suffix}"] = l_tasks_raw
                if l == lang:
                    mission_item["tasks_detailed"] = [
                        {"keyword": "Mission", "task": t} for t in l_tasks_raw
                    ]
            synergy_missions.append(mission_item)

    return synergy_missions


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
    is_friend: bool = False,
) -> Dict[str, Any]:
    try:
        loc = get_localized_data(lang)
        UI = loc.get("UI_STRINGS", {})

        # 1. Validation: Check if birth dates are valid YYYY-MM-DD
        if not birth_date_str or not re.match(r"^\d{4}-\d{2}-\d{2}", birth_date_str):
            return {"error": UI.get("invalid_date_msg", "Please enter a valid birth date (YYYY-MM-DD).")}
            
        # For friend mode, the partner date is mandatory and must be valid
        if is_friend:
            if not idol_birth_date or not re.match(r"^\d{4}-\d{2}-\d{2}", idol_birth_date):
                return {"error": UI.get("invalid_partner_date_msg", "Please enter a valid partner/friend birth date (YYYY-MM-DD).")}
        # In star mode, if idol_birth_date is provided (even if optional), validate its format
        elif idol_birth_date and not re.match(r"^\d{4}-\d{2}-\d{2}", idol_birth_date):
            return {"error": UI.get("invalid_partner_date_msg", "Please enter a valid birth date format (YYYY-MM-DD).")}

        dominant = calc_dominant(birth_date_str)
        user_weights = calc_element_weights(birth_date_str)
        idol_dominant = calc_dominant(idol_birth_date) if idol_birth_date else None

        user_el = UI.get("element_labels", {}).get(dominant, dominant)
        idol_el = (
            UI.get("element_labels", {}).get(idol_dominant, idol_dominant)
            if idol_dominant
            else user_el
        )

        user_seed = f"{birth_date_str}{gender}"
        random.seed(_hash_seed(user_seed))

        # 1. User Saju Analysis
        user_saju = _get_user_saju(dominant, user_weights, user_mbti, lang, UI)

        partner_word = (
            UI.get("friend_word", "Friend")
            if is_friend
            else UI.get("star_word", "Star")
        )
        display_idol = idol_name if idol_name else partner_word
        display_user = UI.get("user_name_fallback", "You")

        # 2. Monthly Fortune
        monthly_fortune = _get_monthly_fortune(
            user_seed,
            display_idol,
            display_user,
            user_el,
            user_el,
            idol_el,
            is_friend,
            partner_word,
            lang,
            loc,
        )

        # 3. Lifetime Fortune
        L_LIFETIME_STAGES = loc.get("LIFETIME_STAGES", {})
        lifetime_fortune = get_segmented_fortune(
            dominant, L_LIFETIME_STAGES, seed_val=f"SEGMENTED_{user_seed}"
        )

        # 4. Chemistry & Missions
        is_pure_saju = (
            not idol_mbti
            or idol_mbti == "Unknown"
            or idol_mbti == UI.get("mbti_unrevealed")
        )
        L_CUR_TIPS = loc.get("PURE_TIPS", []) if is_pure_saju else loc.get("TIPS", [])
        idol_mbti_fallback = (
            UI.get("pure_saju_label", "🌟 Deep Soul Ripple")
            if is_pure_saju
            else (idol_mbti if idol_mbti else UI.get("mbti_unrevealed"))
        )

        base_score = calculate_synergy_score(
            dominant,
            idol_dominant if idol_dominant else dominant,
            birth_date_str,
            idol_birth_date if idol_birth_date else birth_date_str,
            user_mbti,
            idol_mbti,
        )

        is_gen = "GEN_MISSION_COMPONENTS" in loc
        synergy_missions = _get_synergy_missions(
            dominant,
            idol_dominant,
            birth_date_str,
            idol_birth_date,
            user_mbti,
            idol_mbti,
            user_seed,
            idol_name,
            partner_word,
            lang,
            loc,
            UI,
            is_friend,
            is_gen,
            base_score,
            display_user,
            display_idol,
            idol_mbti_fallback,
            user_el,
            idol_el,
        )

        # 5. MZ Report Synthesis
        fragments = loc.get("MZ_ANALYSIS_FRAGMENTS", {})
        mz_report = assemble_mz_report(
            fragments,
            dominant,
            idol_dominant if idol_dominant else dominant,
            user_mbti,
            idol_mbti,
            base_score,
            idol_name,
            lang,
            UI=UI,
            user_name=display_user,
            is_friend=is_friend,
            partner_word=partner_word,
        )

        sh_seed = f"SHUFFLE_{user_seed}_{idol_name}"
        combo_seed = _hash_seed(f"DYN_TIPS_{user_seed}_{idol_name}_{dominant}_{idol_dominant}")
        user_saju_mock = {'dominant_element': user_el}
        idol_saju_mock = {'dominant_element': idol_el}
        selected_tips = _generate_dynamic_tips(user_saju_mock, idol_saju_mock, user_mbti, idol_mbti, lang, is_friend, combo_seed, loc)

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
            "missionMotivation": mz_report.get("missionMotivation", ""),
            "synergy": mz_report["relationship"],
            "tips": selected_tips,
            "base_synergy_score": base_score,
            "synergy_missions": synergy_missions,
        }

        return {
            "dominant_element": dominant,
            "user_saju_content": user_saju["content"],
            "user_saju": user_saju,
            "monthly_fortune": monthly_fortune,
            "lifetime_fortune": lifetime_fortune,
            "chemistry_signal": chemistry_signal,
            "mz_saju_dictionary": loc.get("MZ_SAJU_DICTIONARY", {}),
            "ui_titles": UI.get("TITLES", {}),
        }

    except Exception as e:
        import traceback

        traceback.print_exc()
        return {"error": "Error in Saju Analysis."}
