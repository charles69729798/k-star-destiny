import requests
import re
import json

API_URL = "http://localhost:8000/api"

def check_korean_residue(text):
    if not text:
        return False
    # 한글 정규표현식
    return bool(re.search("[가-힣]", str(text)))

def run_integrity_test(user, star_name, lang):
    params = {
        "birth_date": user["birth_date"],
        "gender": user["gender"],
        "user_mbti": user["mbti"],
        "idol_name": star_name,
        "lang": lang
    }
    
    try:
        # 1. Search Star
        search_res = requests.get(f"{API_URL}/idol/search", params={"name": star_name}, timeout=30)
        idol_data = search_res.json().get("data", {})
        
        # 2. Analyze
        payload = {**params, "idol_mbti": idol_data.get("mbti", ""), "idol_birth_date": idol_data.get("birth_date", "")}
        analyze_res = requests.get(f"{API_URL}/saju/analyze", params=payload, timeout=30)
        result = analyze_res.json().get("analysis", {})
        
        # 3. Validation
        if lang != "ko":
            residues = []
            def scan(obj):
                if isinstance(obj, str):
                    if check_korean_residue(obj):
                        residues.append(obj)
                elif isinstance(obj, list):
                    for item in obj: scan(item)
                elif isinstance(obj, dict):
                    for k, v in obj.items(): scan(v)
            
            scan(result)
            if residues:
                print(f"❌ [FAIL] {lang} mode has Korean residue: {residues[:2]}...")
                return False
        
        print(f"✅ [PASS] {lang} mode integrity secured for {star_name}")
        return True
    except Exception as e:
        print(f"⚠️ [ERROR] {e}")
        return False

if __name__ == "__main__":
    # Sample Test for James (EN) match with Wonyoung
    james = {"birth_date": "1995-12-25", "gender": "male", "mbti": "INTJ"}
    run_integrity_test(james, "Wonyoung", "en")
