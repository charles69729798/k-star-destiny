import asyncio
import httpx
import json

API_BASE_URL = "http://localhost:8000/api"

test_cases = [
    {"id": "TC-01", "name": "정국", "expected": "1997-09-01"},
    {"id": "TC-02", "name": "고윤정", "expected": "1996-04-22"},
    {"id": "TC-03", "name": "Karina", "expected": "2000-04-11"},
    {"id": "TC-04", "name": "Rosalía", "expected": "1992-09-25"},
    {"id": "TC-05", "name": "UnknownPersonXYZ999", "expected": "not_found"}
]

async def run_test():
    print("🚀 Starting K-Saju AI Search QA Test Suite...\n")
    async with httpx.AsyncClient(timeout=30.0) as client:
        for tc in test_cases:
            print(f"[{tc['id']}] Testing: {tc['name']}...")
            try:
                response = await client.get(f"{API_BASE_URL}/idol/search", params={"name": tc['name']})
                data = response.json()
                
                if data.get("status") == "success":
                    result = data.get("data", {})
                    birth_date = result.get("birth_date", "N/A")
                    mbti = result.get("mbti", "N/A")
                    print(f"  ✅ SUCCESS | Found: {birth_date} | MBTI: {mbti}")
                else:
                    print(f"  ⚠️ INFO | {data.get('status')}: {data.get('message', 'No data found')}")
                    
            except Exception as e:
                print(f"  ❌ ERROR | Request failed: {e}")
            print("-" * 40)

if __name__ == "__main__":
    asyncio.run(run_test())
