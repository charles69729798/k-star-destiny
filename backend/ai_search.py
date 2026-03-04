import json
import os
from run_search import search

def search_idol_perplexity(name: str, wiki_title: str = "", wiki_lang: str = "en"):
    """
    내부 모듈을 직접 호출하여 Wikipedia + 나무위키 검색을 수행합니다.
    (기존 subprocess 방식에서 모듈 임포트 방식으로 변경하여 hot-reload 시의 에러 방지)
    """
    print(f"🔍 [AI Search] Searching for: {name} | wiki_title={wiki_title}")

    try:
        data = search(name, wiki_title, wiki_lang)
        if data:
            print(f"  ✅ Output received: {data.get('name')}")
            return data
        else:
            print(f"  ❌ Search Failed.")
            return None
    except Exception as e:
        print(f"  ❌ Search Error: {e}")
        return None
