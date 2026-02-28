import sys
import os
import json

# Add backend directory to path
sys.path.append(os.path.dirname(__file__))

from saju_engine import analyze_destiny

def test_manual_mbti_uat():
    print("🎯 Targeted UAT: Manual Star MBTI Input & Saju Calendar")
    
    # Test Parameters
    birth_date = "1998-05-12"
    gender = "female"
    user_mbti = "ENFP"
    idol_name = "장원영" # Jang Wonyoung from pool
    manual_idol_mbti = "INFJ" # Manually override her ENTJ
    idol_birth = "2004-08-31"
    
    languages = ["ko", "en"]
    
    for lang in languages:
        print(f"\n--- Testing Language: {lang.upper()} ---")
        result = analyze_destiny(
            birth_date_str=birth_date,
            gender=gender,
            user_mbti=user_mbti,
            idol_name=idol_name,
            idol_mbti=manual_idol_mbti,
            idol_birth_date=idol_birth,
            lang=lang
        )
        
        if "error" in result:
            print(f"❌ Error in {lang}: {result['error']}")
            continue

        # 1. Check Monthly Fortune (Calendar)
        monthly = result.get("monthly_fortune", [])
        print(f"📅 Monthly Fortune (Calendar) Count: {len(monthly)}")
        if len(monthly) == 12:
            print(f"   Sample (Month 1): {monthly[0]['keyword']} - {monthly[0]['desc'][:30]}...")
        else:
            print("   ❌ Monthly fortune count IS NOT 12!")

        # 2. Check Chemistry Signal & Manual MBTI
        chem = result.get("chemistry_signal", {})
        revealed_mbti = chem.get("idol_mbti")
        print(f"✨ Star Revealed MBTI in Result: {revealed_mbti}")
        
        if revealed_mbti == manual_idol_mbti:
            print(f"   ✅ Manual MBTI ({manual_idol_mbti}) correctly reflected in analysis.")
        else:
            print(f"   ❌ MBTI Mismatch! Expected {manual_idol_mbti}, got {revealed_mbti}")

        # 3. Check Lifetime Fortune
        print(f"🔮 Lifetime Fortune: {result.get('lifetime_fortune', '')[:50]}...")

    print("\n✅ Targeted UAT Finished.")

if __name__ == "__main__":
    test_manual_mbti_uat()
