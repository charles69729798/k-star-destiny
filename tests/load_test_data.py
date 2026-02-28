from backend.saju_engine import analyze_destiny
import json

# 1. Virtual Users (10)
users = [
    {"name": "Alice (USA)", "birth_date": "1998-05-15", "gender": "female", "mbti": "ENFP"},
    {"name": "Bruno (Brazil)", "birth_date": "2001-11-20", "gender": "male", "mbti": "ISTP"},
    {"name": "Chandra (Indonesia)", "birth_date": "1995-02-10", "gender": "female", "mbti": "INFJ"},
    {"name": "Diego (Mexico)", "birth_date": "2003-08-05", "gender": "male", "mbti": "ENTP"},
    {"name": "Elena (Russia)", "birth_date": "1999-12-31", "gender": "female", "mbti": "ISFJ"},
    {"name": "Fahmi (Thailand)", "birth_date": "2000-04-22", "gender": "male", "mbti": "ESTJ"},
    {"name": "Gabi (Argentina)", "birth_date": "1997-07-14", "gender": "female", "mbti": "ESFP"},
    {"name": "Hassan (Egypt)", "birth_date": "1996-03-03", "gender": "male", "mbti": "INTJ"},
    {"name": "Iris (UK)", "birth_date": "2002-09-18", "gender": "female", "mbti": "INFP"},
    {"name": "Jin (Vietnam)", "birth_date": "1994-01-25", "gender": "male", "mbti": "ENFJ"},
]

# 2. Virtual Idols (10)
idols = [
    {"name": "BTS Jungkook", "birth_date": "1997-09-01", "gender": "male", "mbti": "ISFP"},
    {"name": "Stray Kids Bang Chan", "birth_date": "1997-10-03", "gender": "male", "mbti": "ENFJ"},
    {"name": "NewJeans Hanni", "birth_date": "2004-10-06", "gender": "female", "mbti": "INFP"},
    {"name": "SEVENTEEN Hoshi", "birth_date": "1996-06-15", "gender": "male", "mbti": "INFP"},
    {"name": "IVE Wonyoung", "birth_date": "2004-08-31", "gender": "female", "mbti": "E???"},
    {"name": "Stray Kids Felix", "birth_date": "2000-09-15", "gender": "male", "mbti": "ESFJ"},
    {"name": "BLACKPINK Lisa", "birth_date": "1997-03-27", "gender": "female", "mbti": "ESFJ"},
    {"name": "BTS RM", "birth_date": "1994-09-12", "gender": "male", "mbti": "INFJ"},
    {"name": "TWICE Sana", "birth_date": "1996-12-29", "gender": "female", "mbti": "ENFP"},
    {"name": "Stray Kids Hyunjin", "birth_date": "2000-03-20", "gender": "male", "mbti": "INFP"},
]

def run_test():
    results = []
    print(f"{'User Name':<20} | {'Dominant Element':<15} | {'MBTI Recommendation'}")
    print("-" * 70)
    
    for user in users:
        # Run backend logic directly
        analysis = analyze_destiny(user["birth_date"], user["gender"])
        results.append({
            "user": user["name"],
            "element": analysis["dominant_element"],
            "mbti_match": analysis["mbti_recommendations"],
            "user_mbti": user["mbti"]
        })
        
        recs = ", ".join(analysis["mbti_recommendations"])
        print(f"{user['name']:<20} | {analysis['dominant_element']:<15} | {recs}")

    # Summary Report
    print("\n" + "="*30)
    print("DESTINY ANALYSIS SUMMARY")
    print("="*30)
    
    element_counts = {}
    for r in results:
        element_counts[r["element"]] = element_counts.get(r["element"], 0) + 1
    
    print("\n1. Energy Distribution (Users):")
    for el, count in element_counts.items():
        print(f" - {el}: {count} users")

    print("\n2. Sample Compatibility Check:")
    # Test User Alice with Jungkook
    alice_analysis = analyze_destiny(users[0]["birth_date"], users[0]["gender"])
    jk_analysis = analyze_destiny(idols[0]["birth_date"], idols[0]["gender"])
    
    print(f" - User {users[0]['name']} ({users[0]['mbti']}) vs {idols[0]['name']} ({idols[0]['mbti']})")
    print(f"   Alice Energy: {alice_analysis['dominant_element']}")
    print(f"   Jungkook Energy: {jk_analysis['dominant_element']}")
    
    if users[0]["mbti"] in jk_analysis["mbti_recommendations"]:
        print("   >>> Result: DESTINY MATCH! Alice's personality fits Jungkook's energy.")
    else:
        print("   >>> Result: Neutral compatibility.")

if __name__ == "__main__":
    run_test()
