
import sys
import os
sys.path.append(os.path.abspath("."))
from saju_engine import analyze_destiny
import json
from collections import Counter

def get_jaccard_similarity(str1, str2):
    if not str1 or not str2: return 0.0
    a = set(str1.split())
    b = set(str2.split())
    intersection = a.intersection(b)
    union = a.union(b)
    return len(intersection) / len(union) if len(union) > 0 else 0.0

def run_comprehensive_test():
    # 3 Users with distinct birthdays and MBTIs
    users = [
        {"id": "U1", "b": "1990-05-15", "g": "female", "m": "INFJ"},
        {"id": "U2", "b": "1995-10-22", "g": "male", "m": "ENTP"},
        {"id": "U3", "b": "2002-01-08", "g": "female", "m": "ISFP"}
    ]
    
    # 10 Stars
    stars = [
        {"n": "Irene", "b": "1991-03-29", "m": "ENTJ"},
        {"n": "Jungkook", "b": "1997-09-01", "m": "ISFP"},
        {"n": "Jennie", "b": "1996-01-16", "m": "INFP"},
        {"n": "Felix", "b": "2000-09-15", "m": "ESFJ"},
        {"n": "Sana", "b": "1996-12-29", "m": "ENFP"},
        {"n": "Wonyoung", "b": "2004-08-31", "m": "ENFP"},
        {"n": "Sakura", "b": "1998-03-19", "m": "INFP"},
        {"n": "Hoshi", "b": "1996-06-15", "m": "INFP"},
        {"n": "Aiko", "b": "2004-02-03", "m": "ENTP"},
        {"n": "Karina", "b": "2000-04-11", "m": "ENFP"}
    ]

    print("=== PART 1: K-Saju & God-Saeng Calendar Analysis (Variable: User) ===")
    user_results = []
    for u in users:
        res = analyze_destiny(u["b"], u["g"], u["m"], stars[0]["n"], stars[0]["m"], stars[0]["b"])
        user_results.append({
            "id": u["id"],
            "saju_content": res["user_saju"]["content"],
            "calendar_content": "|".join([m["desc"] for m in res["monthly_fortune"]])
        })
    
    # Compare Saju & Calendar similarity between users
    for i in range(len(user_results)):
        for j in range(i + 1, len(user_results)):
            saju_sim = get_jaccard_similarity(user_results[i]["saju_content"], user_results[j]["saju_content"])
            cal_sim = get_jaccard_similarity(user_results[i]["calendar_content"], user_results[j]["calendar_content"])
            print(f"Compare {user_results[i]['id']} vs {user_results[j]['id']}: Saju Similarity: {saju_sim:.2f}, Calendar Similarity: {cal_sim:.2f}")

    print("\n=== PART 2: Destiny Signal Analysis (3 Users x 10 Stars = 30 Matches) ===")
    matches = []
    for u in users:
        for s in stars:
            res = analyze_destiny(u["b"], u["g"], u["m"], s["n"], s["m"], s["b"])
            sig = res["chemistry_signal"]
            report_text = f"{sig['relationship']} {sig['bias']} {sig['tmi']} {sig['recentFortune']} {sig['synergy']}"
            matches.append({
                "u": u["id"],
                "s": s["n"],
                "text": report_text,
                "score": sig["base_synergy_score"]
            })
    
    # Analyze similarity across 30 matches
    sim_scores = []
    for i in range(len(matches)):
        for j in range(i + 1, len(matches)):
            sim = get_jaccard_similarity(matches[i]["text"], matches[j]["text"])
            sim_scores.append(sim)
            
    avg_sim = sum(sim_scores) / len(sim_scores)
    max_sim = max(sim_scores)
    min_sim = min(sim_scores)
    
    print(f"Total Matches Analyzed: {len(matches)}")
    print(f"Average Similarity: {avg_sim:.2f}")
    print(f"Max Similarity: {max_sim:.2f}")
    print(f"Min Similarity: {min_sim:.2f}")

if __name__ == "__main__":
    run_comprehensive_test()
