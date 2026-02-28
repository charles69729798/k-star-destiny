import sys
import os
# Add current directory to path
sys.path.append(os.getcwd())
sys.path.append(os.path.join(os.getcwd(), 'backend'))

from backend.saju_engine import analyze_destiny
import json

def test_saju():
    print("Testing Saju Engine...")
    
    params = {
        "birth_date_str": "1995-10-13",
        "gender": "male",
        "user_mbti": "ENFJ",
        "idol_name": "Jimin",
        "idol_mbti": "ENFJ",
        "idol_birth_date": "1995-10-13"
    }
    
    langs = ["ko", "en", "fr"]
    
    for lang in langs:
        print(f"\n--- Testing Language: {lang} ---")
        try:
            res = analyze_destiny(lang=lang, **params)
            if "error" in res:
                print(f"Error: {res['error']}")
                continue
                
            print(f"Dominant Element: {res.get('dominant_element')}")
            print(f"Summary: {res.get('user_saju', {}).get('summary')}")
            
            lifetime = res.get('lifetime_fortune')
            print(f"Lifetime Fortune: {lifetime[:80]}..." if lifetime else "Lifetime Fortune: None")
            
            missions = res.get('chemistry_signal', {}).get('synergy_missions', [])
            print(f"Synergy Missions Count: {len(missions)}")
            if missions:
                print(f"Sample Mission Label: {missions[0].get('label')}")
                
            dict_data = res.get('mz_saju_dictionary', {})
            print(f"MZ Dictionary Title: {dict_data.get('title')}")
            
        except Exception as e:
            print(f"Exception during {lang} test: {e}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    test_saju()
