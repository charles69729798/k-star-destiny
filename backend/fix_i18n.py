import saju_i18n
import json
import codecs

I18N = saju_i18n.I18N_DATA

en_guides = {
    'vibe': [
        'Sync your mood with {idol} today',
        'Share a similar aesthetic online',
        "Listen to {idol}'s recommended playlist"
    ],
    'heart': [
        'Send a supportive message to {idol}',
        'Celebrate their recent achievements',
        'Write down what you love about {idol}'
    ],
    'energy': [
        "Match {idol}'s high energy today",
        'Challenge yourself to something new',
        'Do a 10-minute workout inspired by them'
    ]
}

es_guides = {
    'vibe': [
        'Sincroniza tu estado de ánimo con {idol} hoy',
        'Comparte una estética similar en línea',
        'Escucha la playlist recomendada de {idol}'
    ],
    'heart': [
        'Envía un mensaje de apoyo a {idol}',
        'Celebra sus logros recientes',
        'Escribe lo que amas de {idol}'
    ],
    'energy': [
        'Iguala la alta energía de {idol} hoy',
        'Ponte a prueba con algo nuevo',
        'Haz un entrenamiento de 10 min inspirado en ellos'
    ]
}

pt_guides = {
    'vibe': [
        'Sincronize seu humor com {idol} hoje',
        'Compartilhe uma estética semelhante online',
        'Ouça a playlist recomendada por {idol}'
    ],
    'heart': [
        'Envie uma mensagem de apoio para {idol}',
        'Comemore suas conquistas recentes',
        'Escreva o que você ama em {idol}'
    ],
    'energy': [
        'Iguale a alta energia de {idol} hoje',
        'Desafie-se a algo novo',
        'Faça um treino de 10 min inspirado neles'
    ]
}

def inject(lang, guides):
    if 'MZ_ANALYSIS_FRAGMENTS' not in I18N[lang]:
        I18N[lang]['MZ_ANALYSIS_FRAGMENTS'] = {}
    I18N[lang]['MZ_ANALYSIS_FRAGMENTS']['action_guides'] = guides
    
    # Remove the bad key from earlier if exists
    if 'MZ_REPORT_FRAGMENTS' in I18N[lang]:
        del I18N[lang]['MZ_REPORT_FRAGMENTS']

inject('en', en_guides)
inject('es', es_guides)
inject('pt', pt_guides)

out = 'from typing import Dict, Any, List\n\nI18N_DATA = ' + json.dumps(I18N, ensure_ascii=False, indent=4) + '\n\n'
out += 'def get_localized_data(lang: str) -> Dict[str, Any]:\n    return I18N_DATA.get(lang, I18N_DATA[\"en\"])\n'

with codecs.open('saju_i18n.py', 'w', 'utf-8') as f:
    f.write(out)

print('Translation for action_guides injected correctly.')

print('-'*30)
print('UAT CHECK RESULTS:')
for lang in ['ko', 'en', 'es', 'pt']:
    guides = I18N[lang].get('MZ_ANALYSIS_FRAGMENTS', {}).get('action_guides', {})
    print(f'[{lang.upper()} action_guides]')
    for k, v in guides.items():
        print(f'  {k}: {v[0]} ...')
