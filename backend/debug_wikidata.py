import requests
from urllib.parse import quote

HEADERS = {"User-Agent": "KDestinyApp/1.0", "Accept": "application/json"}

# IU Wikipedia QID 조회 확인
r = requests.get(
    "https://en.wikipedia.org/w/api.php?action=query&titles=IU+(entertainer)&prop=pageprops&ppprop=wikibase_item&format=json",
    headers=HEADERS, timeout=8
)
pages = r.json().get("query", {}).get("pages", {})
qid = None
for p in pages.values():
    qid = p.get("pageprops", {}).get("wikibase_item")
print("QID:", qid)

# Wikidata Entity API로 직접 조회 (SPARQL 대신)
if qid:
    r2 = requests.get(
        f"https://www.wikidata.org/wiki/Special:EntityData/{qid}.json",
        headers=HEADERS, timeout=10
    )
    entity = r2.json().get("entities", {}).get(qid, {})
    claims = entity.get("claims", {})

    # P569: 생일
    p569 = claims.get("P569", [])
    if p569:
        val = p569[0].get("mainsnak", {}).get("datavalue", {}).get("value", {})
        print("birthdate raw:", val)

    # P21: 성별
    p21 = claims.get("P21", [])
    if p21:
        gender_qid = p21[0].get("mainsnak", {}).get("datavalue", {}).get("value", {}).get("id", "")
        print("gender QID:", gender_qid)
        # Q6581072 = female, Q6581097 = male
        gender_map = {"Q6581072": "female", "Q6581097": "male"}
        print("gender:", gender_map.get(gender_qid, "unknown"))
