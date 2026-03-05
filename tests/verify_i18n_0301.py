import backend.saju_i18n as i
d = i.I18N_DATA
for lang in ['en', 'es', 'pt', 'ko']:
    tip_cnt = len(d[lang].get('TIP_COMPONENTS', {}).get('actions', []))
    mis_cnt = len(d[lang].get('MISSION_COMPONENTS', {}).get('labels', []))
    print(f"{lang}: TIP_actions={tip_cnt}, MISSION_labels={mis_cnt}")
print("saju_i18n.py 파싱 성공!")
