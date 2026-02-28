import sys
import os
import json
import time

# 백엔드 경로 추가
sys.path.append(os.path.dirname(__file__))

from ai_search import search_idol_perplexity

def test_search(name):
    print(f"--- Testing search for: {name} ---")
    start_time = time.time()
    result = search_idol_perplexity(name)
    end_time = time.time()
    
    print(f"Elapsed Time: {end_time - start_time:.2f} seconds")
    if result:
        print("✅ Result Found:")
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print("❌ No Result Found or Timeout")

if __name__ == "__main__":
    test_search("IU")
    print("\n" + "="*30 + "\n")
    test_search("아이유")
