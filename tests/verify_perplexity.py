import asyncio
import sys
import os

# Add backend to path
sys.path.append(os.path.join(os.getcwd(), 'backend'))

from ai_search import search_idol_perplexity

async def verify_perplexity():
    print("🧪 [Internal Verification] Testing Perplexity AI Search...")
    
    # Test Case: Park Bo-gum (The one that failed before)
    print("\n[Test] Searching for '박보검' via Perplexity AI...")
    result = await search_idol_perplexity("박보검")
    
    if result:
        print(f"✅ SUCCESS: {result['birth_date']} | MBTI: {result['mbti']} | Gender: {result['gender']}")
    else:
        print("❌ FAILED: Could not find data for 박보검")

    # Test Case: Rosalía (Multilingual test)
    print("\n[Test] Searching for 'Rosalía'...")
    result_r = await search_idol_perplexity("Rosalía")
    if result_r:
        print(f"✅ SUCCESS: {result_r['birth_date']} | MBTI: {result_r['mbti']}")
    else:
        print("❌ FAILED: Could not find data for Rosalía")

if __name__ == "__main__":
    asyncio.run(verify_perplexity())
