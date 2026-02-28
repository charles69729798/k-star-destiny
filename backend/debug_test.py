import sys
import os
import json

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from run_search import get_candidates, search
from saju_engine import analyze_destiny

def test_search(name):
    print(f"--- Testing Search for: {name} ---")
    try:
        candidates = get_candidates(name)
        print(f"Candidates found: {len(candidates)}")
        for c in candidates:
            print(f" - {c['title']} (Person: {c['is_person']}, Lang: {c['lang']})")
        
        if candidates:
            top = candidates[0]
            print(f"Searching for top candidate: {top['title']}")
            # result = search(name, top['title'], top['lang']) # search() prints to stdout, no return
    except Exception as e:
        print(f"Error in search test: {e}")

def test_analyze():
    print("\n--- Testing Analysis ---")
    try:
        # User: 1993-05-16, Male, ENTJ
        # Idol: IU (1993-05-16), INFJ
        result = analyze_destiny(
            birth_date_str="1993-05-16",
            gender="male",
            user_mbti="ENTJ",
            idol_name="아이유",
            idol_mbti="INFJ",
            idol_birth_date="1993-05-16",
            lang="ko"
        )
        print("Analysis Keys:", result.keys())
        if "error" in result:
            print("Error Result:", result["error"])
        else:
            print("Success: Analysis generated.")
    except Exception as e:
        print(f"Error in analyze test: {e}")

if __name__ == "__main__":
    test_search("아이유")
    test_analyze()
