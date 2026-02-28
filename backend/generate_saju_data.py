import json
import random

# Saju Theme Templates
themes = [
    {"kw_ko": "목왕상", "kw_en": "Wood Vitality", "kw_es": "Vitalidad de Madera", "kw_pt": "Vitalidade de Madeira", "desc_ko": "새로운 시작의 기운이 강하며 창의적인 아이디어가 샘솟는 달입니다.", "desc_en": "Strong energy of new beginnings with creative ideas overflowing this month.", "desc_es": "Fuerte energía de nuevos comienzos con ideas creativas desbordantes este mes.", "desc_pt": "Forte energia de novos começos com ideias criativas transbordando este mês."},
    {"kw_ko": "화왕상", "kw_en": "Fire Peak", "kw_es": "Pico de Fuego", "kw_pt": "Pico de Fogo", "desc_ko": "열정과 에너지가 정점에 달해 추진하는 일마다 큰 성과가 예상됩니다.", "desc_en": "Passion and energy hit their peak, promising great results in all endeavors.", "desc_es": "La pasión y la energía alcanzan su punto máximo, prometendo grandes resultados.", "desc_pt": "A paixão e a energia atingem seu pico, prometendo grandes resultados em tudo."},
    {"kw_ko": "금왕상", "kw_en": "Metal Harvest", "kw_es": "Cosecha de Metal", "kw_pt": "Colheita de Metal", "desc_ko": "결실을 맺는 시기이며 금전적인 이득과 보상이 따르는 풍요로운 달입니다.", "desc_en": "A time of harvest with financial gains and rewards bringing abundance.", "desc_es": "Tiempo de cosecha con ganancias financieras y recompensas que traen abundancia.", "desc_pt": "É tempo de colheita, com ganhos financeiros e recompensas trazendo abundância."},
    {"kw_ko": "수왕상", "kw_en": "Water Wisdom", "kw_es": "Sabiduría de Agua", "kw_pt": "Sabedoria de Água", "desc_ko": "내실을 다지고 지혜를 쌓기에 좋으며 통찰력이 날카로워지는 시기입니다.", "desc_en": "Perfect for internal growth and wisdom, a time when your insight sharpens.", "desc_es": "Perfecto para el crecimiento interno y la sabiduría, tu intuición se vuelve aguda.", "desc_pt": "Perfeito para o crescimento interno e sabedoria; sua intuição se torna afiada."},
    {"kw_ko": "식신생재", "kw_en": "Wealth Flow", "kw_es": "Flujo de Riqueza", "kw_pt": "Fluxo de Riqueza", "desc_ko": "자신의 기술과 재능이 부로 연결되는 원활한 경제적 흐름이 감지됩니다.", "desc_en": "A smooth flow where your skills and talents translate directly into wealth.", "desc_es": "Un flujo suave donde tus habilidades y talentos se traducen en riqueza.", "desc_pt": "Um fluxo suave onde suas habilidades e talentos se traduzem em riqueza."},
    {"kw_ko": "관인상생", "kw_en": "Honor Boost", "kw_es": "Aumento de Honor", "kw_pt": "Aumento de Honra", "desc_ko": "사회적 명예와 인정이 따르며 윗사람이나 조직의 도움을 받는 운입니다.", "desc_en": "Social honor and recognition follow, with support from mentors or organizations.", "desc_es": "Sigue el honor y reconocimiento social, con apoyo de mentores u organizaciones.", "desc_pt": "Honra e reconhecimento social seguem, com apoio de mentores ou organizações."},
    {"kw_ko": "비겁조력", "kw_en": "Strong Alliance", "kw_es": "Alianza Fuerte", "kw_pt": "Aliança Forte", "desc_ko": "동료나 친구의 도움으로 난관을 극복하고 공동의 목표를 달성하는 달입니다.", "desc_en": "Overcome obstacles and achieve common goals with a colleague's or friend's help.", "desc_es": "Supera obstáculos y logra metas comunes con la ayuda de colegas o amigos.", "desc_pt": "Supere obstáculos e alcance metas comuns com a ajuda de colegas ou amigos."},
    {"kw_ko": "인성보필", "kw_en": "Supportive Aura", "kw_es": "Aura de Soporte", "kw_pt": "Aura de Suporte", "desc_ko": "학문이나 문서 계약에서 길운이 따르며 귀인의 가르침을 얻게 됩니다.", "desc_en": "Good fortune in studies or contracts, gaining wisdom from a mentor.", "desc_es": "Buena fortuna en estudios o contratos, obteniendo sabiduría de um mentor.", "desc_pt": "Boa sorte em estudos ou contratos, ganhando sabedoria de um mentor."},
    {"kw_ko": "역마살기운", "kw_en": "Dynamic Move", "kw_es": "Movimiento Dinámico", "kw_pt": "Movimento Dinâmico", "desc_ko": "이동수나 변화의 기운이 강하며 여행이나 출장에서 새로운 기회를 만납니다.", "desc_en": "Strong energy of movement and change; find new opportunities in travel.", "desc_es": "Fuerte energía de movimiento y cambio; encuentra nuevas oportunidades viajando.", "desc_pt": "Forte energia de movimento e mudança; encontre novas oportunidades viajando."},
    {"kw_ko": "도화발동", "kw_en": "Charisma On", "kw_es": "Carisma Activado", "kw_pt": "Carisma Ativado", "desc_ko": "인간관계에서 매력이 돋보이며 대중의 주목을 한 몸에 받는 시기입니다.", "desc_en": "Your charm stands out in social circles, drawing the public's full attention.", "desc_es": "Tu carisma resalta en círculos sociales, atrayendo la atención del público.", "desc_pt": "Seu carisma se destaca em círculos sociais, atraindo a atenção do público."}
]

# Generate variations to reach 50 sets
final_data = []
for i in range(50):
    t = themes[i % len(themes)]
    idx = (i // len(themes)) + 1
    final_data.append({
        "kw_ko": f"{t['kw_ko']} {idx}" if idx > 1 else t['kw_ko'],
        "kw_en": f"{t['kw_en']} {idx}" if idx > 1 else t['kw_en'],
        "kw_es": f"{t['kw_es']} {idx}" if idx > 1 else t['kw_es'],
        "kw_pt": f"{t['kw_pt']} {idx}" if idx > 1 else t['kw_pt'],
        "desc_ko": t['desc_ko'].replace("달입니다", f"{idx}차 호운의 달입니다") if idx > 1 else t['desc_ko'],
        "desc_en": t['desc_en'].replace("month", f"month (Phase {idx})") if idx > 1 else t['desc_en'],
        "desc_es": t['desc_es'].replace("mes", f"mes (Fase {idx})") if idx > 1 else t['desc_es'],
        "desc_pt": t['desc_pt'].replace("mês", f"mês (Fase {idx})") if idx > 1 else t['desc_pt'],
    })

# Format for Python injection
output = {
    "ko": {"keywords": [d['kw_ko'] for d in final_data], "descs": [d['desc_ko'] for d in final_data]},
    "en": {"keywords": [d['kw_en'] for d in final_data], "descs": [d['desc_en'] for d in final_data]},
    "es": {"keywords": [d['kw_es'] for d in final_data], "descs": [d['desc_es'] for d in final_data]},
    "pt": {"keywords": [d['kw_pt'] for d in final_data], "descs": [d['desc_pt'] for d in final_data]}
}

print(json.dumps(output, ensure_ascii=False, indent=2))
