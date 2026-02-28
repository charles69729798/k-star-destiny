import sys
import os
sys.path.append(os.getcwd())
from saju_engine import analyze_destiny
import json

def test():
    print("Testing Monthly Fortune Generation...")
    res = analyze_destiny(
        birth_date_str="1995-10-13",
        gender="male",
        user_mbti="ENFP",
        idol_name="Wonyoung",
        idol_mbti="ENTJ",
        idol_birth_date="2004-08-31",
        lang="ko"
    )
    
    monthly = res.get('monthly_fortune', [])
    print(f"Monthly Fortune Count: {len(monthly)}")
    if monthly:
        print("First month sample:", monthly[0])
    else:
        print("FAILED: Monthly fortune is empty!")

if __name__ == "__main__":
    test()
