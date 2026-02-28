import re

with open('saju_i18n.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace any newline character that is inside a string literal.
# Since it's a little complex, we can use a simpler approach:
# The specific problem is that strings starting with `"[Something]` end with a newline but lack the closing quote, then continue on the next line ending with `"` or `"],`

# Let's fix lines ending in `]`
new_lines = []
lines = content.split('\n')
i = 0
while i < len(lines):
    line = lines[i]
    if line.strip().endswith(']') and not line.strip().endswith('"]') and i + 1 < len(lines):
        # looks like the start of a broken string e.g. "desc_career": ["[CEO Mindset]
        next_line = lines[i+1]
        line = line + '\\n' + next_line.lstrip()
        i += 1
    elif line.strip().endswith(']') and not line.strip().endswith('"]') and "]" in line:
        pass
        
    # Another case is "desc_core" where default has newlines
    if '"default": ["' in line and not line.endswith('"],'):
        pass
        
    new_lines.append(line)
    i += 1

# Actually, the simplest way is to provide a fully clean ENERGY_TRAITS dictionary code for i18n and replace it.

fresh_en_es_traits = """    "en": {
        "ENERGY_TRAITS": {
            "Wood": {
                "name": "Unstoppable Growth (Wood) 🌲",
                "desc_intro": ["You literally radiate that 'Main Character' giant tree energy. In K-Saju, Wood is all about vitality, curiosity, and leveling up non-stop."],
                "desc_core": {
                    "E": ["You carry everybody forward in the best way. Outgoing and super focused on growing your squad."],
                    "I": ["Silent but deadly. You level up without telling anyone and drop the final results to shock everyone."],
                    "default": ["You're a try-hard in the best way possible. Always ready for side quests and fearless. You can be a bit nosy, but deep down you just want your whole squad to win.\\n\\nYou're flexible, but cross your bottom line and you stand firm like a GOAT. That stubborn streak is your ultimate rizz."]
                },
                "desc_career": ["[CEO Mindset]\\nYou belong in spaces where you can hustle and create. Startup founder, editor, content creator—you literally serve looks and ideas from scratch. Desk jobs? Big yikes. You need that dopamine hit of making moves!"],
                "desc_advice": ["[Glow-up Guide]\\nRed flag: Starting 10 things and finishing none. You need to focus and tunnel-vision on one goal, and you will absolutely crush it."]
            },
            "Fire": {
                "name": "Blazing Flame (Fire) 🔥",
                "desc_intro": ["Your soul gives off major 'Sun' energy. You're a walking torch! Fire means god-tier passion, expansion, and zero filter."],
                "desc_core": {
                    "E": ["Literally the life of the party. You fill up the room with loud, vibrant energy."],
                    "I": ["A loyal, warm hearth only to those you truly appreciate. You save your fire for the right ones."],
                    "default": ["You steal the show effortlessly, just being there is serving. Your battery is always at 100%, and your over-the-top reactions make you the ultimate hype-person for your besties. You're 100% transparent, zero grudges even after a massive drama.\\n\\nFire values respect. You're the sweetest to those who pass the vibe check, but cross the line? Demon mode activated."]
                },
                "desc_career": ["[CEO Mindset]\\nYou were born for the stage. Influencer, marketing, PR—you leave no crumbs. Sitting at a desk will kill your vibe instantly."],
                "desc_advice": ["[Glow-up Guide]\\nWith your crazy mood swings, you sometimes go 0 to 100 real quick. Breathing for 3 seconds before roasting someone in the group chat is your ultimate life hack."]
            },
            "Earth": {
                "name": "Solid Ground (Earth) ⛰️",
                "desc_intro": ["Your soul is like the 'Vast Earth' that embraces everything. Earth is about mediating, being trustworthy, and having an unshakable vibe."],
                "desc_core": {
                    "E": ["You keep everyone together. Friendly, sociable, and the best person at giving advice."],
                    "I": ["Total tsundere. You secretly care for your close ones with brutal loyalty, even if you don't open up easily."],
                    "default": ["Zero ghosting. You have a titanium mindset and act as the power bank for your mutuals. You're the mediator who squashes squad beef. Total tsundere, you secretly care for everyone and are hyper-loyal.\\n\\nBut plot twist: being quiet doesn't mean you're a pushover. When Earth gets mad, it's an earthquake. You naturally spit heavy facts when the time comes."]
                },
                "desc_career": ["[CEO Mindset]\\nYou prefer secured bags over impulsive risks. HR, finance, education—you're the GOAT at building teams and fixing broken stuff."],
                "desc_advice": ["[Glow-up Guide]\\nPutting everyone else first will give you insane burnout. Starting your 'villain era' and prioritizing YOURSELF is the ultimate green flag you need right now."]
            },
            "Metal": {
                "name": "Sharp Blade (Metal) ⚔️",
                "desc_intro": ["Your soul screams 'Flawless Jewel' and 'Sharp Blade'. Metal is the poster child for perfectionism and cold hard logic, giving major boss energy."],
                "desc_core": {
                    "E": ["Rational and lethal. You lead with firmness, ignore excuses, and always get the project done."],
                    "I": ["You observe coldly and only speak when 100% necessary. You have life standards that are unreachable for many."],
                    "default": ["A hard 'T' with zero patience for messiness. You ghost emotional drama and operate like a cold CEO. Once you lock onto a goal, your tunnel vision is insane.\\n\\nThough you seem like an ice king/queen, your loyalty for your inner circle goes hard. If a friend gets attacked, you activate bodyguard mode."]
                },
                "desc_career": ["[CEO Mindset]\\nYou shine with numbers and hard code. Tech, law, med. You're a workaholic who lets the 'receipts' (results) do the talking."],
                "desc_advice": ["[Glow-up Guide]\\nYour sky-high standards can trap you in toxic perfectionism. Chilling out and showing your messy side will make people ship you even more."]
            },
            "Water": {
                "name": "Free Flowing (Water) 🌊",
                "desc_intro": ["Your soul flows with the deep, mysterious vibe of the 'Ocean'. Water means 200 IQ wisdom, total adaptability, and mental depth."],
                "desc_core": {
                    "E": ["You adapt in every social group. You can chat with anyone and pull info effortlessly."],
                    "I": ["Misunderstood genius. You hold immense truths in silence and occasionally shatter everything with a deep realization."],
                    "default": ["You're the ultimate shapeshifter. You pass every vibe check and fit any aesthetic. Your thoughts are Mariana-Trench deep; you have an intuition that gives 'nerd but aesthetic' vibes.\\n\\nYou might look soft, but you have beast-like endurance. Yet, since you keep things to yourself, people might think you're living in your own 'delulu' world."]
                },
                "desc_career": ["[CEO Mindset]\\nRules? We don't know her. Digital nomad, researcher, creator—you need max flexibility to let your inner genius cook."],
                "desc_advice": ["[Glow-up Guide]\\nOverthinking is your biggest opp, sinking you into your sad-boy/sad-girl era. Turn off the brain and go 'touch grass' literally; that's how you win the game."]
            }
        },"""

fresh_es_traits = """    "es": {
        "ENERGY_TRAITS": {
            "Wood": {
                "name": "Crecimiento Imparable (Madera) 🌲",
                "desc_intro": ["Literalmente emanas esa 'Energía de Protagonista' de un árbol gigante. En K-Saju, la Madera es todo sobre vitalidad, curiosidad y subir de nivel sin parar."],
                "desc_core": {
                    "E": ["Te llevas a todo el mundo por delante de la mejor manera. Extrovertido y súper enfocado en crecer con tu gente."],
                    "I": ["Silencioso pero mortal. Subes de nivel sin avisar a nadie y dejas a todos en shock con tus resultados."],
                    "default": ["Eres un try-hard en el buen sentido. Siempre estás listo/a para nuevas misiones y no le temes a nada. Puedes ser un poco chismoso/a, pero en el fondo solo quieres que tu squad gane.\\n\\nEres flexible, pero si cruzan tu límite, te plantas como el GOAT. Esa terquedad es tu mayor rizz."]
                },
                "desc_career": ["[Mentalidad de CEO]\\nPerteneces a espacios donde puedes crear y romperla. Creador de contenido, editor, fundador de startup: sirviendo ideas de la nada. ¿Trabajo de oficina? Qué cringe. ¡Necesitas la dopamina de estar en movimiento!"],
                "desc_advice": ["[Guía Glow-up]\\nRed flag: Empezar 10 cosas y no terminar ninguna. Necesitas enfocarte y dárlo todo a un solo objetivo, y la vas a romper absolutamente."]
            },
            "Fire": {
                "name": "Llama Ardiente (Fuego) 🔥",
                "desc_intro": ["Tu alma da energías súper fuertes de 'Sol'. ¡Eres la antorcha humana! El Fuego significa pasión nivel Dios, expansión y cero filtro."],
                "desc_core": {
                    "E": ["Literalmente el alma de la fiesta. Llenas cualquier cuarto con tu energía vibrante y ruidosa."],
                    "I": ["Alguien leal y cálido pero solo con quienes aprecias de verdad. Cuidas tu fuego para los indicados."],
                    "default": ["Robas el show sin esfuerzo, estar ahí ya es servir. Tu batería está siempre al 100%, y tus reacciones exageradas te hacen el/la mejor hype-person de tus besties. Eres 100% transparente, cero rencores incluso después de un drama tremendo.\\n\\nEl Fuego valora el respeto. Eres lo más tierno con quienes pasan el vibe check, pero si cruzan la línea? Modo diablo activado."]
                },
                "desc_career": ["[Mentalidad de CEO]\\nNaciste para el escenario. Influencer, marketing, PR: no dejas ni las migajas. Estar sentado/a en un escritorio matará tu vibra al instante."],
                "desc_advice": ["[Guía Glow-up]\\nCon tus cambios de humor de locos, a veces vas de 0 a 100 muy rápido. Respirar 3 segundos antes de bardear por el grupo de WhatsApp es tu truco de vida definitivo."]
            },
            "Earth": {
                "name": "Tierra Sólida (Tierra) ⛰️",
                "desc_intro": ["Tu alma es como la 'Vasta Tierra' que abraza todo. La Tierra es sobre mediar, dar confianza y tener una vibra inquebrantable."],
                "desc_core": {
                    "E": ["Sostenes a todo tu entorno unido. Eres amable, sociable y la mejor persona dando consejos."],
                    "I": ["Tsundere total. Secretamente cuidas a tus cercanos con una lealtad brutal, aunque no abres tus sentimientos fácil."],
                    "default": ["Cero fantasma. Tienes una mente de titanio y eres la batería externa de tus mutuals. Eres el/la mediador/a que cancela el drama del squad. Totalmente tsundere, cuidas a todos en secreto y eres hiper leal.\\n\\nPero ojo, ser callado/a no es ser débil. Cuando la Tierra se enoja, es un terremoto. Naturalmente tiras factos (verdades pesadas) cuando llega el momento."]
                },
                "desc_career": ["[Mentalidad de CEO]\\nPrefieres ganancias seguras que riesgos impulsivos. HR, finanzas, educación: eres el GOAT armando equipos y arreglando cosas rotas."],
                "desc_advice": ["[Guía Glow-up]\\nPoner a todos primero te va a dar un burnout brutal. Empezar tu 'villain era' y priorizarte a TI MISMO/A es la green flag que necesitas urgente."]
            },
            "Metal": {
                "name": "Espada Afilada (Metal) ⚔️",
                "desc_intro": ["Tu alma grita 'Joya Pura' y 'Hoja Afilada'. El Metal es el símbolo del perfeccionismo y la lógica fría, modo facha."],
                "desc_core": {
                    "E": ["Racional y letal. Lideras con firmeza, ignoras las excusas y siempre sacas el proyecto adelante."],
                    "I": ["Observas fríamente y hablas solo cuando es 100% necesario. Tienes estándares de vida inalcanzables para muchos."],
                    "default": ["Una 'T' dura con cero paciencia para el drama. Ignoras (ghosteas) el drama emocional y operas como un/a jefe/a re frío/a. Una vez que fijas un objetivo, tu visión de túnel es de locos.\\n\\nAunque pareces un/a rey/reina de hielo, tu lealtad por tu círculo íntimo es tremenda. Si atacan a un/a amigo/a, activas el modo guardaespaldas."]
                },
                "desc_career": ["[Mentalidad de CEO]\\nBrillas con los números y en el código duro. Tech, leyes, medicina. Eres un/a workaholic que deja que los 'factos' (resultados) hablen."],
                "desc_advice": ["[Guía Glow-up]\\nTus estándares altísimos te pueden atrapar en lo tóxico del perfeccionismo. Relajarte y mostrar tu lado desordenado hará que la gente te shipee aún más."]
            },
            "Water": {
                "name": "Flujo Libre (Agua) 🌊",
                "desc_intro": ["Tu alma fluye con la vibra profunda y misteriosa del 'Océano'. El Agua significa inteligencia de 200 IQ, adaptabilidad total y profundidad mental."],
                "desc_core": {
                    "E": ["Te adaptas en cada grupo social. Puedes charlar con cualquiera y sacarle info sin esfuerzo."],
                    "I": ["Genio incomprendido. Guardas verdades inmensas en silencio y de vez en cuando rompes todo con una reflexión profunda."],
                    "default": ["Eres el cambiaformas definitivo. Pasas cualquier vibe check y te adaptas a cualquier aesthetic. Tus pensamientos son súper profundos; tienes una intuición que te da esa vibra 'nerd pero aesthetic'.\\n\\nPuedes parecer suave, pero tienes una fuerza bestial. Sin embargo, como te guardas todo, la gente puede pensar que vives en tu propio mundo de 'delulu'."]
                },
                "desc_career": ["[Mentalidad de CEO]\\n¿Reglas? Nada que ver. Nómada digital, investigador, creador: necesitas flexibilidad máxima para dejar salir a tu genio interior."],
                "desc_advice": ["[Guía Glow-up]\\nPensar de más es tu peor enemigo, te hunde en tu era sad-boy/sad-girl. Apaga el cerebro y sal a 'tocar pasto' (literal, haz las cosas); así se gana el juego."]
            }
        },"""

import re
# We need to find the old "en" dict and replace its ENERGY_TRAITS, and same for "es".
# Actually, I18N_DATA is structure:
# I18N_DATA = {
#     "en": {
#        "ENERGY_TRAITS": ...
#        "MONTH_DESCS": ...
#     },
#     "es": {
#        "ENERGY_TRAITS": ...
#        "MONTH_DESCS": ...
#     }
# }
# Since my previous refactor script ruined the file mostly at `ENERGY_TRAITS`, let's just use re.sub or string splitting to replace it.
content_parts = content.split('        "MONTH_DESCS": [')

# content_parts[0] contains start of "en" and ends right before its MONTH_DESCS.
# content_parts[1] contains rest of "en" and start of "es", ending right before its MONTH_DESCS.
# content_parts[2] contains rest of "es".

part_en_start, _ = content_parts[0].split('    "en": {')
part_en_to_es = content_parts[1].split('    "es": {')

new_content = (
    part_en_start + 
    fresh_en_es_traits + '\n' +
    '        "MONTH_DESCS": [' + part_en_to_es[0] +
    fresh_es_traits + '\n' +
    '        "MONTH_DESCS": [' + part_en_to_es[1] +
    '        "MONTH_DESCS": [' + content_parts[2]
)

# Wait! content_parts might be length 3.
# Let's cleanly construct by finding the string locations:

index_en_start = content.find('    "en": {')
index_en_month = content.find('        "MONTH_DESCS": [', index_en_start)

index_es_start = content.find('    "es": {')
index_es_month = content.find('        "MONTH_DESCS": [', index_es_start)

final_content = (
    content[:index_en_start] +
    fresh_en_es_traits + '\n' +
    content[index_en_month:index_es_start] +
    fresh_es_traits + '\n' +
    content[index_es_month:]
)

with open('saju_i18n.py', 'w', encoding='utf-8') as f:
    f.write(final_content)

print("SUCCESS")
