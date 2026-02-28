import requests
from urllib.parse import quote
import re

HEADERS = {"User-Agent": "KDestinyApp/1.0", "Accept": "application/json"}

# IU Wikipedia 우선 검색
r = requests.get(
    "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=IU&format=json&srlimit=3",
    headers=HEADERS, timeout=8
)
hits = r.json().get("query", {}).get("search", [])
print("search hits:", [h["title"] for h in hits])

page_title = hits[0]["title"] if hits else "IU (entertainer)"
print("using page:", page_title)

# QID 조회
r2 = requests.get(
    f"https://en.wikipedia.org/w/api.php?action=query&titles={quote(page_title)}&prop=pageprops&ppprop=wikibase_item&format=json",
    headers=HEADERS, timeout=8
)
pages = r2.json().get("query", {}).get("pages", {})
qid = None
for p in pages.values():
    qid = p.get("pageprops", {}).get("wikibase_item")
print("QID:", qid)

if qid:
    entity_url = f"https://www.wikidata.org/wiki/Special:EntityData/{qid}.json"
    r3 = requests.get(entity_url, headers=HEADERS, timeout=10)
    entity = r3.json().get("entities", {}).get(qid, {})
    claims = entity.get("claims", {})

    p21 = claims.get("P21", [])
    print("P21 claims:", p21)
    if p21:
        val = p21[0].get("mainsnak", {}).get("datavalue", {}).get("value", {})
        print("P21 value type:", type(val), val)
        if isinstance(val, dict):
            g_qid = val.get("id", "")
            print("gender QID:", g_qid)
