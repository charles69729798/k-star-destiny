import re
import json

def generate_data():
    themes = [
        {"kw_ko": "목왕상", "kw_en": "Wood Vitality", "kw_es": "Vitalidad de Madera", "kw_pt": "Vitalidade de Madeira", "desc_ko": "[목왕상] 새로운 씨앗: 만물이 소생하는 기운이 당신의 일에 생기를 불어넣습니다. 새로운 프로젝트를 시작하기에 완벽한 달입니다.", "desc_en": "[Wood Vitality] New Seeds: The energy of all things reviving breathes life into your work. A perfect month to start new projects.", "desc_es": "[Vitalidad de Madera] Nuevas Semillas: La energía del renacimiento da vida a tu trabajo. Un mes perfecto para iniciar nuevos proyectos.", "desc_pt": "[Vitalidade de Madeira] Novas Sementes: A energia do renascer dá vida ao seu trabalho. Um mês perfeito para iniciar novos projetos."},
        {"kw_ko": "화왕상", "kw_en": "Fire Peak", "kw_es": "Pico de Fuego", "kw_pt": "Pico de Fogo", "desc_ko": "[화왕상] 열정의 폭발: 에너지가 정점에 달합니다. 미뤄왔던 일을 강력한 추진력으로 해결하며 큰 성과를 거두는 달입니다.", "desc_en": "[Fire Peak] Explosion of Passion: Energy reaches its zenith. Resolve long-pending tasks with powerful momentum and achieve great results.", "desc_es": "[Pico de Fuego] Explosión de Pasión: La energía llega a su cenit. Resuelve tareas pendientes con un impulso poderoso y logra grandes resultados.", "desc_pt": "[Pico de Fogo] Explosão de Paixão: A energia atinge o seu auge. Resolva tarefas pendentes com um impulso poderoso e alcance grandes resultados."},
        {"kw_ko": "금왕상", "kw_en": "Metal Harvest", "kw_es": "Cosecha de Metal", "kw_pt": "Colheita de Metal", "desc_ko": "[금왕상] 냉철한 결단: 무엇을 버리고 무엇을 취할지 명확해집니다. 불필요한 인연이나 일을 정리하고 핵심에 집중할 때 부가 쌓입니다.", "desc_en": "[Metal Harvest] Cool Decision: It becomes clear what to discard and what to take. Wealth accumulates when you focus on the core.", "desc_es": "[Cosecha de Metal] Decisión Fría: Se vuelve claro qué descartar y qué tomar. La riqueza se acumula cuando te enfocas en lo esencial.", "desc_pt": "[Colheita de Metal] Decisão Fria: Torna-se claro o que descartar e o que manter. A riqueza acumula-se quando você se foca no essencial."},
        {"kw_ko": "수왕상", "kw_en": "Water Wisdom", "kw_es": "Sabiduría de Agua", "kw_pt": "Sabedoria de Água", "desc_ko": "[수왕상] 깊은 지혜의 축적: 내면의 에너지를 비축하고 지식을 쌓는 시기. 당신의 통찰력이 그 어느 때보다 날카워집니다.", "desc_en": "[Water Wisdom] Accumulation of Wisdom: A time to stockpile inner energy and knowledge. Your insight becomes sharper than ever.", "desc_es": "[Sabiduría de Agua] Acumulación de Sabiduría: Tiempo de almacenar energía interna y conocimiento. Tu intuición es más aguda que nunca.", "desc_pt": "[Sabedoria de Água] Acumulação de Sabedoria: Tempo de armazenar energia interna e conhecimento. Sua intuição está mais afiada do que nunca."},
        {"kw_ko": "식신생재", "kw_en": "Creative Wealth", "kw_es": "Riqueza Creativa", "kw_pt": "Riqueza Criativa", "desc_ko": "[식신생재] 부의 선순환: 당신의 아이디어가 돈으로 바뀌는 흐름이 매우 원활합니다. 투자나 부업에서 좋은 결과가 예상됩니다.", "desc_en": "[Wealth Flow] Virtuous Cycle: The flow of your ideas turning into money is very smooth. Good results expected in investments or side hustles.", "desc_es": "[Flujo de Riqueza] Ciclo Virtuoso: El flujo de tus ideas convirtiéndose en dinero es muy fluido. Se esperan buenos resultados en inversiones.", "desc_pt": "[Fluxo de Riqueza] Ciclo Virtuoso: O fluxo das suas ideias transformando-se em dinheiro é muito fluido. Esperam-se bons resultados em investimentos."},
        {"kw_ko": "관인상생", "kw_en": "Honor & Trust", "kw_es": "Honor y Confianza", "kw_pt": "Honra e Confiança", "desc_ko": "[관인상생] 인정과 승진: 상사나 조직의 신뢰를 한 몸에 받습니다. 책임감 있는 모습이 더 큰 기회로 이어지는 달입니다.", "desc_en": "[Honor & Trust] Recognition & Promotion: Gain the full trust of leaders or organizations. Your responsibility leads to bigger opportunities.", "desc_es": "[Honor y Confianza] Reconocimiento y Ascenso: Gana la plena confianza de líderes. Tu responsabilidad lleva a mayores oportunidades.", "desc_pt": "[Honra e Confiança] Reconhecimento e Promoção: Ganhe a total confiança de líderes. Sua responsabilidade leva a maiores oportunidades."},
        {"kw_ko": "진신발동", "kw_en": "True Essence", "kw_es": "Esencia Verdadera", "kw_pt": "Essência Verdadeira", "desc_ko": "[진신발동] 본연의 매력: 당신만의 독보적인 가치가 세상에 드러납니다. 숨겨왔던 재능이 빛을 발하며 많은 이들을 매료시킵니다.", "desc_en": "[True Essence] Native Charm: Your unique value is revealed to the world. Hidden talents shine, captivating many people.", "desc_es": "[Esencia Verdadera] Encanto Nativo: Tu valor único se revela al mundo. Talentos ocultos brillan, cautivando a mucha gente.", "desc_pt": "[Essência Verdadeira] Encanto Nativo: Seu valor único é revelado ao mundo. Talentos ocultos brilham, cativando muitas pessoas."},
        {"kw_ko": "인덕충만", "kw_en": "Noble Support", "kw_es": "Soporte Noble", "kw_pt": "Suporte Nobre", "desc_ko": "[인덕충만] 귀인의 도움: 혼자 고민하던 문제가 주변의 도움으로 단숨에 해결됩니다. 감사하는 마음이 더 큰 복을 불러옵니다.", "desc_en": "[Noble Support] Help from Mentors: Problems you worried about alone are solved instantly with help. Gratitude brings more luck.", "desc_es": "[Soporte Noble] Ayuda de Mentores: Problemas que te preocupaban se resuelven al instante con ayuda. La gratitud trae más suerte.", "desc_pt": "[Suporte Nobre] Ajuda de Mentores: Problemas que o preocupavam resolvem-se instantaneamente com ajuda. Gratidão traz mais sorte."},
        {"kw_ko": "역마역동", "kw_en": "Dynamic Shift", "kw_es": "Cambio Dinámico", "kw_pt": "Mudança Dinâmica", "desc_ko": "[역마역동] 새로운 지평: 정체되었던 흐름이 깨지고 새로운 변화가 시작됩니다. 이사, 이직, 혹은 새로운 취미가 당신의 삶을 바꿉니다.", "desc_en": "[Dynamic Shift] New Horizons: Stagnant flows break and new changes begin. A move, job change, or new hobby transforms your life.", "desc_es": "[Cambio Dinámico] Nuevos Horizontes: Flujos estancados se rompen y comienzan cambios. Un traslado o nuevo hobby transforma tu vida.", "desc_pt": "[Mudança Dinâmica] Novos Horizontes: Fluxos estagnados quebram e novas mudanças começam. Uma mudança ou novo hobby transforma sua vida."},
        {"kw_ko": "백화요란", "kw_en": "Floral Radiance", "kw_es": "Brillo Floral", "kw_pt": "Brilho Floral", "desc_ko": "[백화요란] 화려한 변신: 당신의 매력이 꽃피는 시기. SNS나 사회적 활동에서 주목받으며 인기가 급상승하는 경험을 합니다.", "desc_en": "[Radiance] Splendid Transformation: A time when your charm blooms. You get noticed in social activities, experiencing a surge in popularity.", "desc_es": "[Radiance] Espléndida Transformación: Tiempo en que tu carisma florece. Te haces notar en actividades sociales.", "desc_pt": "[Radiance] Esplêndida Transformação: Tempo em que seu carisma floresce. Você se destaca em atividades sociais."}
    ]
    
    final_data = []
    for i in range(50):
        t = themes[i % len(themes)]
        idx = (i // len(themes)) + 1
        suffix = f" (Level {idx})" if idx > 1 else ""
        final_data.append({
            "ko": {"kw": f"{t['kw_ko']}{suffix}", "desc": t['desc_ko'].replace("달입니다", f"달입니다{suffix}") if idx > 1 else t['desc_ko']},
            "en": {"kw": f"{t['kw_en']}{suffix}", "desc": t['desc_en'] + suffix},
            "es": {"kw": f"{t['kw_es']}{suffix}", "desc": t['desc_es'] + suffix},
            "pt": {"kw": f"{t['kw_pt']}{suffix}", "desc": t['desc_pt'] + suffix}
        })
    return final_data

def update_file():
    data = generate_data()
    with open('saju_i18n.py', 'r', encoding='utf-8') as f:
        content = f.read()

    langs = ['en', 'ko', 'es', 'pt']
    
    for lang in langs:
        keywords = [d[lang]['kw'] for d in data]
        descs = [d[lang]['desc'] for d in data]
        
        # Format lists
        kw_str = json.dumps(keywords, ensure_ascii=False, indent=12).replace('[', '[\n            ').replace(']', '\n        ]')
        ds_str = json.dumps(descs, ensure_ascii=False, indent=12).replace('[', '[\n            ').replace(']', '\n        ]')
        
        # Regex replacement for specific language section
        # We need to find the specific language block. 
        # For simplicity in this script, we'll look for "MONTH_KEYWORDS": [...] within that lang's block
        # This is a bit tricky with simple regex if the file is complex.
        # But we know the order: en(1), ko(490), es(???), pt(900+)
        
        if lang == 'en':
            start_search = 0
            end_search = 450
        elif lang == 'ko':
            start_search = 450
            end_search = 850
        elif lang == 'es':
            start_search = 800
            end_search = 1100
        elif lang == 'pt':
            start_search = 900
            end_search = 1500
        else:
            continue

        lang_block = content[start_search:end_search]
        
        # Replace MONTH_KEYWORDS
        lang_block = re.sub(r'"MONTH_KEYWORDS":\s*\[.*?\]', f'"MONTH_KEYWORDS": {kw_str}', lang_block, flags=re.DOTALL)
        # Replace MONTH_DESCS
        lang_block = re.sub(r'"MONTH_DESCS":\s*\[.*?\]', f'"MONTH_DESCS": {ds_str}', lang_block, flags=re.DOTALL)
        
        content = content[:start_search] + lang_block + content[end_search:]

    with open('saju_i18n.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully updated saju_i18n.py with 50 sets for each language.")

if __name__ == "__main__":
    update_file()
