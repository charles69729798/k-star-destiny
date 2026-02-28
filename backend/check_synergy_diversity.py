
import sys
import os
sys.path.append(os.path.abspath("."))
from saju_engine import analyze_destiny
import json

def run_simulation():
    # 10 virtual users
    users = [
        {"b": "1990-01-01", "g": "female", "m": "INFJ"},
        {"b": "1995-03-15", "g": "male", "m": "ENTP"},
        {"b": "2000-06-20", "g": "female", "m": "ISFP"},
        {"b": "1988-11-30", "g": "male", "m": "INTJ"},
        {"b": "1992-07-04", "g": "female", "m": "ENFP"},
        {"b": "1999-12-31", "g": "male", "m": "ISTP"},
        {"b": "2003-02-14", "g": "female", "m": "ESFJ"},
        {"b": "1985-09-09", "g": "male", "m": "INTP"},
        {"b": "1997-04-25", "g": "female", "m": "ENTJ"},
        {"b": "1994-08-08", "g": "male", "m": "ISFJ"}
    ]
    
    # 10 stars (mixed)
    stars = [
        {"n": "Irene", "b": "1991-03-29", "m": "ENTJ"},
        {"n": "Jungkook", "b": "1997-09-01", "m": "ISFP"},
        {"n": "Jennie", "b": "1996-01-16", "m": "INFP"},
        {"n": "Felix", "b": "2000-09-15", "m": "ESFJ"},
        {"n": "Sana", "b": "1996-12-29", "m": "ENFP"},
        {"n": "Wonyoung", "b": "2004-08-31", "m": "E"}, # MBTI partial
        {"n": "Sakura", "b": "1998-03-19", "m": "INFP"},
        {"n": "Hoshi", "b": "1996-06-15", "m": "INFP"},
        {"n": "Aiko", "b": "2004-02-03", "m": "Unknown"}, # MBTI unknown
        {"n": "Karina", "b": "2000-04-11", "m": "ENFP"}
    ]
    
    results = []
    task_signatures = []
    
    print(f"{'No':<3} | {'User':<15} | {'Star':<12} | {'Score':<5} | {'Tasks Signature'}")
    print("-" * 80)
    
    for i in range(10):
        u = users[i]
        s = stars[i]
        res = analyze_destiny(u["b"], u["g"], u["m"], s["n"], s["m"], s["b"])
        missions = res["chemistry_signal"]["synergy_missions"]
        
        # Create a signature of tasks to check for duplication
        all_tasks = []
        for m in missions:
            all_tasks.extend(m["tasks"])
        
        sig = "|".join(sorted(all_tasks))
        task_signatures.append(sig)
        
        print(f"{i+1:<3} | {u['m']}({u['b']}) | {s['n']:<12} | {res['chemistry_signal']['base_synergy_score']:<5} | {sig[:40]}...")

    unique_sigs = set(task_signatures)
    redundancy = (1 - len(unique_sigs) / len(task_signatures)) * 100
    
    print("-" * 80)
    print(f"Total Combinations: {len(task_signatures)}")
    print(f"Unique Task Sets: {len(unique_sigs)}")
    print(f"Redundancy Rate: {redundancy:.1f}%")

if __name__ == "__main__":
    run_simulation()
