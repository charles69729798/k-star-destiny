import subprocess
import json
import sys
import os

def search_idol_perplexity(name: str, wiki_title: str = "", wiki_lang: str = "en"):
    """
    별도의 프로세스(run_search.py)를 실행하여 Wikipedia + 나무위키 검색을 수행합니다.
    wiki_title이 있으면 사용자가 선택한 확정 항목으로 정확 조회합니다.
    """
    print(f"🔍 [Subprocess] Searching for: {name} | wiki_title={wiki_title}")

    try:
        script_path = os.path.join(os.path.dirname(__file__), "run_search.py")

        # wiki_title이 있으면 인자로 전달
        args = [sys.executable, script_path, name]
        if wiki_title:
            args.append(wiki_title)
            args.append(wiki_lang)

        result = subprocess.run(
            args,
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=60  # 45초에서 60초로 연장
        )

        if result.returncode == 0 and result.stdout.strip():
            print(f"  ✅ Output received: {result.stdout.strip()[:100]}...")
            try:
                data = json.loads(result.stdout.strip())
                return data  # 부분 데이터도 반환
            except json.JSONDecodeError as e:
                print(f"  ❌ JSON Decode Error: {e}")
                print(f"  ❌ Raw Output: {result.stdout.strip()[:500]}")
        else:
            print(f"  ❌ Subprocess Failed. ReturnCode: {result.returncode}")
            if result.stderr:
                print(f"  ❌ STDERR: {result.stderr[:500]}")

        return None

    except subprocess.TimeoutExpired as e:
        print(f"  ⚠️ Subprocess Timeout (60s) for: {name}")
        if e.stdout:
            print(f"  Partial STDOUT: {e.stdout.decode('utf-8', errors='ignore')[:300]}")
        if e.stderr:
            print(f"  Partial STDERR: {e.stderr.decode('utf-8', errors='ignore')[:300]}")
        return None
    except Exception as e:
        print(f"  ❌ Subprocess Error: {e}")
        return None
