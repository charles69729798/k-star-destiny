import sys, os
sys.path.insert(0, r'c:\InsuranceProject\Sajuapp\backend')
from run_search import get_candidates
import json

print("=== IU 후보 테스트 ===")
cands = get_candidates('IU')
for c in cands:
    print(f"[{'사람' if c.get('is_person') else '비사람'}] {c['title'][:40]} | {c.get('description','')[:60]}")

print("\n=== 장원영 후보 테스트 ===")
cands2 = get_candidates('장원영')
for c in cands2:
    print(f"[{'사람' if c.get('is_person') else '비사람'}] {c['title'][:40]} | {c.get('description','')[:60]}")
