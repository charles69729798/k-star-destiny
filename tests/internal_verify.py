import asyncio
import sys
import os

# Add backend to path
sys.path.append(os.path.join(os.getcwd(), 'backend'))

from ai_search import search_idol_google

async def verify_code():
    print("🧪 [Internal Verification] Testing Code Logic Directly...")
    
    # Test Case: Go Yoon-jung (Known difficult case)
    print("\n[Test] Searching for '고윤정' via Playwright...")
    result = await search_idol_google("고윤정")
    
    if result:
        print(f"✅ FOUND: {result['birth_date']} | MBTI: {result['mbti']}")
    else:
        print("❌ FAILED: Could not find data for 고윤정")

    # Test Case: Park Bo-gum
    print("\n[Test] Searching for '박보검' via Playwright...")
    result_p = await search_idol_google("박보검")
    if result_p:
        print(f"✅ FOUND: {result_p['birth_date']}")
    else:
        print("❌ FAILED: Could not find data for 박보검")

if __name__ == "__main__":
    asyncio.run(verify_code())
