import sys
import json
import re
import datetime
import requests
from urllib.parse import quote

# 한글 출력 인코딩
sys.stdout.reconfigure(encoding='utf-8')

# 공통 요청 헤더 (Wikipedia 권장)
HEADERS = {
    "User-Agent": "KDestinyApp/1.0 (kpop-saju educational project; contact@example.com)",
    "Accept": "application/json",
    "Accept-Language": "ko,en",
}

# ──────────────────────────────────────────
# 언어 감지
# ──────────────────────────────────────────
def is_korean(text: str) -> bool:
    return bool(re.search(r'[가-힣]', text))


# ──────────────────────────────────────────
# Wikipedia REST API (생일 + 성별)
# ──────────────────────────────────────────
def search_wikipedia(name: str, result: dict):
    """Wikipedia REST API + Wikidata Entity API로 생일/성별을 가져옵니다.
    완전 무료, 인증 불필요, 동시 요청 완전 안전.
    """
    # 검색 우선 언어 결정
    if is_korean(name):
        lang_order = ["ko", "en"]
    else:
        lang_order = ["en", "ko"]

    for lang in lang_order:
        try:
            # 1단계: 검색어로 Wikipedia 문서 제목 찾기
            search_url = (
                f"https://{lang}.wikipedia.org/w/api.php"
                f"?action=query&list=search&srsearch={quote(name)}"
                f"&format=json&srlimit=3&srnamespace=0"
            )
            r = requests.get(search_url, headers=HEADERS, timeout=10) # 8에서 10으로 상향
            r.raise_for_status()
            hits = r.json().get("query", {}).get("search", [])
            if not hits:
                continue

            page_title = hits[0]["title"]
            print(f"  [Wiki/{lang}] Found page: {page_title}", file=sys.stderr)

            # 2단계: Wikidata Entity API로 생일 + 성별 가져오기 (최우선)
            _fetch_wikidata_birth(page_title, lang, result)

            # 3단계: 아직 생일/성별이 없으면 REST API 텍스트로 보조 파싱
            if not result["birth_date"] or result["gender"] == "unknown":
                summary_url = (
                    f"https://{lang}.wikipedia.org/api/rest_v1/page/summary/{quote(page_title)}"
                )
                r2 = requests.get(summary_url, headers=HEADERS, timeout=10) # 8에서 10으로 상향
                if r2.status_code == 200:
                    data = r2.json()
                    extract = data.get("extract", "")
                    desc = data.get("description", "").lower()
                    if not result["birth_date"]:
                        parse_birth_date(extract, result)
                    if result["gender"] == "unknown":
                        parse_gender_from_desc(desc + " " + extract, result)

            if result["birth_date"]:
                return  # 생일 찾으면 다음 언어 시도 불필요

        except Exception as e:
            print(f"  [Wiki/{lang}] Error: {e}", file=sys.stderr)
            continue



def _fetch_wikidata_birth(page_title: str, lang: str, result: dict):
    """Wikidata Entity API로 생일(P569) + 성별(P21)을 가져옵니다.
    SPARQL보다 더 빠르고 안정적입니다.
    """
    try:
        # Wikipedia 페이지에서 Wikidata QID 조회
        wd_url = (
            f"https://{lang}.wikipedia.org/w/api.php"
            f"?action=query&titles={quote(page_title)}&prop=pageprops"
            f"&ppprop=wikibase_item&format=json"
        )
        r = requests.get(wd_url, headers=HEADERS, timeout=10) # 6에서 10으로 상향
        pages = r.json().get("query", {}).get("pages", {})
        qid = None
        for p in pages.values():
            qid = p.get("pageprops", {}).get("wikibase_item")
            break

        if not qid:
            return

        # Wikidata Entity API로 직접 조회 (SPARQL보다 빠르고 안정적)
        entity_url = f"https://www.wikidata.org/wiki/Special:EntityData/{qid}.json"
        r2 = requests.get(entity_url, headers={**HEADERS, "Accept": "application/json"}, timeout=15) # 10에서 15로 상향
        r2.raise_for_status()

        entity = r2.json().get("entities", {}).get(qid, {})
        claims = entity.get("claims", {})

        # P569: 생년월일 (형식: "+1993-05-16T00:00:00Z")
        if not result["birth_date"]:
            p569 = claims.get("P569", [])
            if p569:
                time_val = p569[0].get("mainsnak", {}).get("datavalue", {}).get("value", {})
                time_str = time_val.get("time", "") if isinstance(time_val, dict) else ""
                # "+1993-05-16T00:00:00Z" → "1993-05-16"
                import re as _re
                m = _re.match(r'\+?(\d{4}-\d{2}-\d{2})', time_str)
                if m:
                    result["birth_date"] = m.group(1)
                    print(f"  [Wikidata] birth_date = {result['birth_date']}", file=sys.stderr)

        # P21: 성별 QID
        # Q6581072 = female, Q6581097 = male
        if result["gender"] == "unknown":
            p21 = claims.get("P21", [])
            if p21:
                gender_qid = p21[0].get("mainsnak", {}).get("datavalue", {}).get("value", {})
                if isinstance(gender_qid, dict):
                    gender_qid = gender_qid.get("id", "")
                GENDER_MAP = {"Q6581072": "female", "Q6581097": "male", "Q1052281": "female", "Q2449503": "male"}
                resolved = GENDER_MAP.get(gender_qid, "unknown")
                if resolved != "unknown":
                    result["gender"] = resolved
                    print(f"  [Wikidata] gender = {result['gender']} (QID:{gender_qid})", file=sys.stderr)

    except Exception as e:
        print(f"  [Wikidata] Error: {e}", file=sys.stderr)




# ──────────────────────────────────────────
# 보조 검색 (Assistant) - 수동 모드일 때 스니펫 검색
# ──────────────────────────────────────────
def get_assistant_info(name: str) -> dict:
    """수동 모드 또는 자동 수집 버튼 클릭 시 DuckDuckGo 검색을 통해 가장 기본 정보(MBTI, 생일 추정)를 긁어옵니다."""
    result = {"birth_date": "", "mbti": ""}
    try:
        # 영어/다국어 검색 결과(MBTI Personality)를 더 잘 잡기 위한 쿼리
        queries = [
            f"{name} MBTI personality type",
            f"{name} 나이 생일 mbti"
        ]
        
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
        
        for q in queries:
            url = f"https://html.duckduckgo.com/html/?q={quote(q)}"
            r = requests.get(url, headers=headers, timeout=12) # 8에서 12로 상향
            if r.status_code == 200:
                text = r.text
                
                # MBTI (Personality Database 등의 'ENFP', 'ESTJ-A' 매칭)
                if not result["mbti"]:
                    mbti_match = re.search(r'\b([EI][SN][TF][JP](?:-[AT])?)\b', text, re.IGNORECASE)
                    if mbti_match:
                        result["mbti"] = mbti_match.group(1).upper()
                        
                # 생일 (YYYY-MM-DD 또는 YYYY년 MM월 DD일)
                if not result["birth_date"]:
                    birth_match = re.search(r'([12]\d{3})[-년\.\s]+([01]?\d)[-월\.\s]+([0123]?\d)[일\.\s]?', text)
                    if birth_match:
                        y, m, d = birth_match.groups()
                        result["birth_date"] = f"{int(y):04d}-{int(m):02d}-{int(d):02d}"
                        
            if result["mbti"] and result["birth_date"]:
                break
                
    except Exception as e:
        print(f"  [Assistant] Error: {e}", file=sys.stderr)
    return result

# ──────────────────────────────────────────
# 나무위키 검색 (MBTI)
# ──────────────────────────────────────────
def search_namuwiki(name: str, result: dict):
    """나무위키에서 MBTI를 가져옵니다.
    영어 이름 입력 시 Wikipedia langlinks로 한국어 이름을 먼저 알아낸 뒤 검색합니다.
    """
    if result["mbti"]:
        return

    # 영어 이름인 경우: Wikipedia에서 한국어 이름 조회
    ko_name = name
    if not is_korean(name):
        try:
            search_url = (
                f"https://en.wikipedia.org/w/api.php"
                f"?action=query&list=search&srsearch={quote(name)}"
                f"&format=json&srlimit=1&srnamespace=0"
            )
            r = requests.get(search_url, headers=HEADERS, timeout=10) # 6에서 10으로 상향
            hits = r.json().get("query", {}).get("search", [])
            if hits:
                page_title = hits[0]["title"]
                # 한국어 위키 링크 조회
                ll_url = (
                    f"https://en.wikipedia.org/w/api.php"
                    f"?action=query&titles={quote(page_title)}&prop=langlinks"
                    f"&lllang=ko&format=json"
                )
                r2 = requests.get(ll_url, headers=HEADERS, timeout=10) # 6에서 10으로 상향
                pages = r2.json().get("query", {}).get("pages", {})
                for p in pages.values():
                    langlinks = p.get("langlinks", [])
                    if langlinks:
                        ko_name = langlinks[0].get("*", name)
                        # 괄호 안 내용 제거: "아이유 (가수)" → "아이유"
                        ko_name = re.sub(r'\s*\(.*\)', '', ko_name).strip()
                        print(f"  [NamuWiki] Korean name resolved: {ko_name}", file=sys.stderr)
                        break
        except Exception as e:
            print(f"  [NamuWiki] Lang lookup failed: {e}", file=sys.stderr)

    # 나무위키 HTML 파싱 (한국어 이름 우선, 원래 이름 폴백)
    for search_name in list(dict.fromkeys([ko_name, name])):
        _search_namuwiki_html(search_name, result)
        if result["mbti"]:
            break




def _search_namuwiki_html(name: str, result: dict):
    """나무위키 HTML 직접 파싱 (API 실패 폴백)"""
    try:
        from bs4 import BeautifulSoup
        # 한국어 이름으로 시도, 실패 시 영어 그대로
        urls = [f"https://namu.wiki/w/{quote(name)}"]
        # 영어 이름인 경우 추가 시도 패턴
        if not is_korean(name):
            urls.append(f"https://namu.wiki/search/{quote(name)}")

        for url in urls:
            r = requests.get(
                url,
                headers={
                    **HEADERS,
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/124.0.0.0",
                    "Referer": "https://namu.wiki/",
                },
                timeout=15, # 10에서 15로 상향
                allow_redirects=True
            )
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, 'html.parser')
                text = soup.get_text(separator=' ')

                # MBTI 파싱 (나무위키는 보통 'INFP', 'ENFJ-T' 형태로 기재)
                if not result["mbti"]:
                    # 'MBTI' 키워드 근처에서 집중 검색
                    mbti_section = re.search(
                        r'MBTI.{0,50}([EI][NS][TF][JP](?:[-\s][AT])?)',
                        text, re.IGNORECASE
                    )
                    if mbti_section:
                        raw = mbti_section.group(1).strip()
                        cleaned = re.sub(r'\s', '-', raw).upper()
                        result["mbti"] = cleaned
                    else:
                        parse_mbti(text, result)

                # 생일/성별 보조 파싱
                if not result["birth_date"]:
                    parse_birth_date(text, result)
                if result["gender"] == "unknown":
                    parse_gender_from_desc(text, result)

                print(f"  [NamuWiki/HTML] MBTI={result['mbti']}", file=sys.stderr)
                if result["mbti"]:
                    break
    except Exception as e:
        print(f"  [NamuWiki/HTML] Error: {e}", file=sys.stderr)


# ──────────────────────────────────────────
# 파싱 유틸리티
# ──────────────────────────────────────────
def parse_birth_date(text: str, data: dict):
    if data["birth_date"]:
        return
    today_year = datetime.date.today().year
    text = re.sub(r'\s+', ' ', text)

    # 1. 한글: 1993년 6월 16일
    m = re.search(r'(\d{4})년\s*(\d{1,2})월\s*(\d{1,2})일', text)
    if m:
        y, mo, d = m.groups()
        if 1900 < int(y) < today_year:
            data["birth_date"] = f"{y}-{mo.zfill(2)}-{d.zfill(2)}"
            return

    # 2. ISO / 점 구분: 1993-06-16 or 1993.06.16
    m = re.search(r'(\d{4})[.\-](\d{1,2})[.\-](\d{1,2})', text)
    if m:
        y, mo, d = m.groups()
        if 1900 < int(y) < (today_year - 1) and 1 <= int(mo) <= 12 and 1 <= int(d) <= 31:
            data["birth_date"] = f"{y}-{mo.zfill(2)}-{d.zfill(2)}"
            return

    # 3. 영어: August 31, 2004 / 31 August 2004
    MONTHS = {
        'january':'01','february':'02','march':'03','april':'04',
        'may':'05','june':'06','july':'07','august':'08',
        'september':'09','october':'10','november':'11','december':'12',
        'jan':'01','feb':'02','mar':'03','apr':'04','jun':'06','jul':'07',
        'aug':'08','sep':'09','oct':'10','nov':'11','dec':'12',
    }
    m = re.search(r'([A-Z][a-z]+)\s+(\d{1,2}),?\s+(\d{4})', text)
    if m:
        mo_s, d, y = m.groups()
        mn = MONTHS.get(mo_s.lower())
        if mn and 1900 < int(y) < today_year:
            data["birth_date"] = f"{y}-{mn}-{d.zfill(2)}"
            return

    m = re.search(r'(\d{1,2})\s+([A-Z][a-z]+)\s+(\d{4})', text)
    if m and not data["birth_date"]:
        d, mo_s, y = m.groups()
        mn = MONTHS.get(mo_s.lower())
        if mn and 1900 < int(y) < today_year:
            data["birth_date"] = f"{y}-{mn}-{d.zfill(2)}"


def parse_mbti(text: str, data: dict):
    if data["mbti"]:
        return
    # MBTI + -A/-T (Assertive/Turbulent)
    m = re.search(r'\b([EI][NS][TF][JP])[\s\-]([AT])\b', text, re.IGNORECASE)
    if m:
        data["mbti"] = f"{m.group(1).upper()}-{m.group(2).upper()}"
        return
    m = re.search(r'\b([EI][NS][TF][JP])\b', text, re.IGNORECASE)
    if m:
        data["mbti"] = m.group(1).upper()


def parse_gender_from_desc(text: str, data: dict):
    """Wikipedia description + K-pop 그룹명으로 성별 추론"""
    if data["gender"] != "unknown":
        return
    lower = text.lower()

    girl = [
        "ive", "아이브", "aespa", "에스파", "newjeans", "뉴진스",
        "le sserafim", "르세라핌", "(여자)아이들", "itzy", "있지", "nmixx",
        "blackpink", "블랙핑크", "twice", "트와이스", "red velvet", "레드벨벳",
        "stayc", "fromis_9", "dreamcatcher", "mamamoo", "loona",
        "girls' generation", "소녀시대", "sistar", "gfriend", "oh my girl",
        "kep1er", "케플러", "babymonster", "illit", "아일릿",
        "cosmic girls", "wjsn", "viviz", "kiss of life",
    ]
    boy = [
        "bts", "방탄소년단", "exo", "엑소", "stray kids", "스트레이 키즈",
        "seventeen", "세븐틴", "txt", "투모로우바이투게더",
        "enhypen", "엔하이픈", "ateez", "에이티즈", "nct", "엔시티",
        "got7", "갓세븐", "monsta x", "astro", "아스트로", "the boyz",
        "treasure", "zerobaseone", "제로베이스원", "riize", "라이즈",
        "boynextdoor", "super junior", "슈퍼주니어", "shinee", "샤이니",
        "bigbang", "빅뱅", "winner", "ikon", "p1harmony",
    ]

    for g in girl:
        if g in lower:
            data["gender"] = "female"
            return
    for g in boy:
        if g in lower:
            data["gender"] = "male"
            return

    # 일반 키워드
    fk = ["south korean singer", "south korean actress", "female", "she ", "her ", "여성", "여자", "걸그룹"]
    mk = ["south korean actor", "south korean rapper", "male", "he ", "his ", "남성", "남자", "보이그룹"]
    fs = sum(1 for k in fk if k in lower)
    ms = sum(1 for k in mk if k in lower)
    if fs > ms:
        data["gender"] = "female"
    elif ms > fs:
        data["gender"] = "male"


# ──────────────────────────────────────────
# 후보 목록 반환 (disambiguation)
# ──────────────────────────────────────────
def get_candidates(name: str) -> list:
    """Wikipedia에서 이름과 일치하는 상위 후보를 반환합니다.
    사람 관련 항목만 필터링하여 선택 UI에 표시합니다.
    """
    lang = "ko" if is_korean(name) else "en"
    candidates = []

    # 사람 관련 키워드 (이 키워드가 포함된 항목만 후보로)
    PERSON_KEYWORDS = [
        "singer", "rapper", "actor", "actress", "idol", "kpop", "k-pop",
        "entertainer", "musician", "artist", "member", "band", "personality", "model",
        "가수", "배우", "아이돌", "랩퍼", "가수", "뮤지션", "아티스트", "연예인", "방송인", "모델",
        "south korean", "한국의", "대한민국의", "출생", "born", "member of",
    ]

    try:
        # 검색 후 상위 5개 후보 가져오기
        search_url = (
            f"https://{lang}.wikipedia.org/w/api.php"
            f"?action=query&list=search&srsearch={quote(name)}"
            f"&format=json&srlimit=5&srnamespace=0"
        )
        r = requests.get(search_url, headers=HEADERS, timeout=10) # 8에서 10으로 상향
        hits = r.json().get("query", {}).get("search", [])

        # 영어로도 추가 검색 (한국어 이름인 경우)
        if is_korean(name):
            r2 = requests.get(
                search_url.replace("ko.wikipedia", "en.wikipedia"),
                headers=HEADERS, timeout=10 # 8에서 10으로 상향
            )
            hits += r2.json().get("query", {}).get("search", [])[:3]

        if not hits:
            return []

        # 각 후보의 summary 정보 가져오기
        seen_titles = set()
        for hit in hits:
            title = hit["title"]
            if title in seen_titles:
                continue
            seen_titles.add(title)

            try:
                summary_url = (
                    f"https://{lang}.wikipedia.org/api/rest_v1/page/summary/{quote(title)}"
                )
                rs = requests.get(summary_url, headers=HEADERS, timeout=5)
                if rs.status_code != 200:
                    # 영어 위키로 재시도
                    summary_url = (
                        f"https://en.wikipedia.org/api/rest_v1/page/summary/{quote(title)}"
                    )
                    rs = requests.get(summary_url, headers=HEADERS, timeout=10) # 5에서 10으로 상향

                if rs.status_code == 200:
                    data = rs.json()
                    description = data.get("description", "")
                    extract = data.get("extract", "")[:200]
                    thumbnail = data.get("thumbnail", {}).get("source", "")

                    # 사람 관련 항목만 포함 (비사람 항목 필터링)
                    combined = (description + " " + extract).lower()
                    person_matches = [kw for kw in PERSON_KEYWORDS if kw in combined]
                    is_person = len(person_matches) > 0
                    print(f"  [Candidates] Item: {title}, matches={person_matches}, is_person={is_person}", file=sys.stderr)

                    # 항상 후보에 포함 (사람 여부로 정렬만)
                    candidates.append({
                        "title": title,
                        "description": description,
                        "extract": extract,
                        "thumbnail": thumbnail,
                        "is_person": is_person,
                        "lang": lang if rs.url.startswith(f"https://{lang}") else "en",
                    })

                    if len(candidates) >= 5:
                        break
            except Exception:
                continue

        # 사람 관련 항목을 앞으로 정렬
        candidates.sort(key=lambda x: (0 if x["is_person"] else 1))
        return candidates

    except Exception as e:
        print(f"[Candidates] Error: {e}", file=sys.stderr)
        return []


def search_by_wiki_title(wiki_title: str, lang: str, name: str) -> dict:
    """확정된 Wikipedia 제목으로 정확하게 데이터를 가져옵니다."""
    result = {
        "name": name,
        "birth_date": "",
        "birth_time": "unknown",
        "gender": "unknown",
        "mbti": ""
    }

    try:
        # Wikidata Entity API로 생일 + 성별 조회
        _fetch_wikidata_birth(wiki_title, lang, result)

        # 보조: REST API summary로 텍스트 파싱
        if not result["birth_date"] or result["gender"] == "unknown":
            summary_url = (
                f"https://{lang}.wikipedia.org/api/rest_v1/page/summary/{quote(wiki_title)}"
            )
            r = requests.get(summary_url, headers=HEADERS, timeout=10) # 8에서 10으로 상향
            if r.status_code == 200:
                data = r.json()
                extract = data.get("extract", "")
                desc = data.get("description", "").lower()
                if not result["birth_date"]:
                    parse_birth_date(extract, result)
                if result["gender"] == "unknown":
                    parse_gender_from_desc(desc + " " + extract, result)

        # 나무위키로 MBTI (확정된 위키 타이틀도 시도, 실패 시 원래 이름 시도)
        if not result["mbti"]:
            search_namuwiki(wiki_title, result)
        if not result["mbti"]:
            search_namuwiki(name, result)

    except Exception as e:
        print(f"[WikiTitle] Error: {e}", file=sys.stderr)

    return result


# ──────────────────────────────────────────
# 메인 진입점
# ──────────────────────────────────────────
def search(name: str, wiki_title: str = "", wiki_lang: str = "en"):
    result = {
        "name": name,
        "birth_date": "",
        "birth_time": "unknown",
        "gender": "unknown",
        "mbti": ""
    }

    print(f"[Search] Starting for: {name}", file=sys.stderr)

    if wiki_title:
        # 확정된 Wikipedia 제목으로 직접 검색
        print(f"[Search] Using wiki_title: {wiki_title}", file=sys.stderr)
        result = search_by_wiki_title(wiki_title, wiki_lang, name)
    else:
        # 일반 검색
        search_wikipedia(name, result)
        search_namuwiki(name, result)

    print(f"[Search] Result: {result}", file=sys.stderr)
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    import sys as _sys
    if len(_sys.argv) > 1:
        name_arg = _sys.argv[1]
        wiki_arg = _sys.argv[2] if len(_sys.argv) > 2 else ""
        lang_arg = _sys.argv[3] if len(_sys.argv) > 3 else "en"
        search(name_arg, wiki_arg, lang_arg)
