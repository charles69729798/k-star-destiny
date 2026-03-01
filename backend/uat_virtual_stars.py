import urllib.request, urllib.parse, json

print("--- 5 VIRTUAL STARS UAT (3x3 Synergey Missions) ---")

user = {'birth_date': '1995-10-13', 'gender': 'female', 'mbti': 'ESTJ'}

virtual_stars = [
    {'name': 'Leo (Supernova)', 'birth_date': '1998-05-15', 'mbti': 'ISFP', 'gender': 'male'},
    {'name': 'Aria (Stardust)', 'birth_date': '2001-11-20', 'mbti': 'ENTJ', 'gender': 'female'},
    {'name': 'Zion (GalaxyX)', 'birth_date': '1996-02-14', 'mbti': 'INFP', 'gender': 'male'},
    {'name': 'Mia (CosmicGirls)', 'birth_date': '2003-08-08', 'mbti': 'ESFP', 'gender': 'female'},
    {'name': 'Kai (Nebula)', 'birth_date': '1999-12-25', 'mbti': 'INTJ', 'gender': 'male'}
]

languages = ['ko', 'en', 'es', 'pt']

for star in virtual_stars:
    print(f"\n=========================================")
    print(f"⭐ TARGET STAR: {star['name']} (MBTI: {star['mbti']})")
    print(f"=========================================")
    
    for lang in languages:
        params = urllib.parse.urlencode({
            'birth_date': user['birth_date'],
            'gender': user['gender'],
            'user_mbti': user['mbti'],
            'idol_name': star['name'],
            'idol_mbti': star['mbti'],
            'idol_birth_date': star['birth_date'],
            'lang': lang
        })
        req = urllib.request.Request(f'http://127.0.0.1:8000/api/saju/analyze?{params}')
        
        try:
            with urllib.request.urlopen(req) as response:
                res = json.loads(response.read().decode())
                missions = res.get('analysis', {}).get('chemistry_signal', {}).get('synergy_missions', [])
                
                print(f"  [{lang.upper()} Language]")
                for m in missions:
                    print(f"    ▶ {m['label']}")
                    for t_idx, t in enumerate(m['tasks']):
                        print(f"      - {t}")
        except Exception as e:
            print(f"  [{lang.upper()}] Failed to call API: {e}")
    print()
