import uvicorn
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, Dict, Any, List
from pydantic import BaseModel
import os
import json
import sys
import subprocess
from dotenv import load_dotenv
import hashlib
from datetime import datetime
import random
from saju_engine import analyze_destiny
from ai_search import search_idol_perplexity
from saju_i18n import MBTI_CHEMISTRY
from apscheduler.schedulers.background import BackgroundScheduler
import git_sync

# Global Stats Persistence
STATS_FILE = "stats.json"
DEFAULT_STATS = {
    "today_challengers": 0, 
    "total_visitors": 0, 
    "last_reset_date": "",
    "voter_ids": [] # Store unique session/browser IDs for the day
}
STATS = DEFAULT_STATS.copy()

def load_stats():
    global STATS
    if os.path.exists(STATS_FILE):
        try:
            with open(STATS_FILE, "r", encoding="utf-8") as f:
                loaded = json.load(f)
                STATS.update(loaded)
                
            # Daily Reset Logic
            current_date = datetime.now().strftime("%Y-%m-%d")
            if STATS.get("last_reset_date") != current_date:
                print(f"🔄 Daily Reset triggered. Previous: {STATS.get('last_reset_date')}, Current: {current_date}")
                STATS["today_challengers"] = 0
                STATS["voter_ids"] = [] # Clear IDs for new day
                STATS["last_reset_date"] = current_date
                save_stats()
        except Exception as e:
            print(f"❌ Error loading stats: {e}")
            STATS = DEFAULT_STATS.copy()

def save_stats():
    try:
        with open(STATS_FILE, "w", encoding="utf-8") as f:
            json.dump(STATS, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"❌ Error saving stats: {e}")

load_stats()
class Comment(BaseModel):
    id: str
    author: str
    handle: str
    content: str
    timestamp: str
    likes: int
    avatar_color: str
    replies: List[Dict[str, Any]] = []

# Mock Comments (YouTube Style)
COMMENTS = [
    {
        "id": "1",
        "author": "SajuLover99",
        "handle": "@saju_master",
        "content": "Wonyoung and I are literally 90% synergy? I'm screaming right now! 🌲🔥",
        "timestamp": "2 hours ago",
        "likes": 124,
        "avatar_color": "#FF6B6B",
        "replies": []
    },
    {
        "id": "2",
        "author": "KpopStan_01",
        "handle": "@destiny_seeker",
        "content": "The analysis is so accurate it's scary. My MBTI and Saju match perfectly with Karina's flow.",
        "timestamp": "5 hours ago",
        "likes": 89,
        "avatar_color": "#4D96FF",
        "replies": []
    }
]

# Load environment variables
load_dotenv()

app = FastAPI(
    title="K-Destiny AI API",
    description="Real-time Saju + MBTI Matching via Wikipedia + 나무위키"
)

# CORS setup
# 환경 변수에 관계없이 모든 도메인/포트에서의 접근을 허용하여 접속 포트 불일치 근본 원인 해결
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Welcome to K-Destiny AI API", "status": "active"}

@app.post("/api/internal/bot-run")
async def run_bot_manually():
    """테스트를 위해 수동으로 봇을 실행하는 엔드포인트"""
    try:
        # 별도 쓰레드에서 실행하여 응답 지연 방지
        import threading
        thread = threading.Thread(target=auto_bot_update)
        thread.start()
        return {"status": "success", "message": "무인 데이터 봇이 수동으로 실행되었습니다. 결과는 이메일로 발송됩니다."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 아이돌 풀 외부 데이터 로드 (idols.json)
IDOLS_FILE = os.path.join(os.path.dirname(__file__), "idols.json")
IDOL_POOL = []

def load_idol_pool():
    global IDOL_POOL
    try:
        if os.path.exists(IDOLS_FILE):
            with open(IDOLS_FILE, "r", encoding="utf-8") as f:
                IDOL_POOL = json.load(f)
                print(f"✅ Loaded {len(IDOL_POOL)} idols from {IDOLS_FILE}")
        else:
            print(f"⚠️ {IDOLS_FILE} not found. Starting with empty pool.")
            IDOL_POOL = []
    except Exception as e:
        print(f"❌ Error loading idols: {e}")
        IDOL_POOL = []

load_idol_pool()

def auto_bot_update():
    """매일 자정 또는 요청 시 실행되는 자동 업데이트 봇"""
    print(f"🤖 [Auto-Bot] Starting scheduled update at {datetime.now()}")
    
    # 1. 기존 데이터 로드
    load_idol_pool()
    original_count = len(IDOL_POOL)
    
    # 2. 데이터 확장 로직 (시뮬레이션: 실제로는 크롤링 또는 AI 검색 루틴이 들어감)
    # 여기서는 예시로 기존 데이터의 정합성을 체크하거나 
    # 새로운 데이터가 idols.json에 외부에서 추가되었을 경우를 대비해 리로딩을 수행합니다.
    # 추후 1단계 제안서의 'AI-Search' 루틴을 호출하여 신규 아이돌을 자동으로 찾게 할 수 있습니다.
    
    new_count = len(IDOL_POOL) - original_count
    
    # 3. Git 역공급 및 이메일 알림 실행
    git_sync.push_to_git(new_count)

# 스케줄러 설정
scheduler = BackgroundScheduler()
# 매일 자정(00:00)에 실행
scheduler.add_job(auto_bot_update, 'cron', hour=0, minute=0)
scheduler.start()
print("⏰ [Scheduler] Background bot started. Job set for 00:00 daily.")




def get_mbti_compatibility(user_mbti: str, idol_mbti: str) -> dict:
    if not user_mbti or not idol_mbti or len(user_mbti) != 4 or len(idol_mbti) != 4:
        return {"score": 50, "label_ko": "보통"}
    
    pair = (user_mbti.upper(), idol_mbti.upper())
    rev_pair = (pair[1], pair[0])
    
    if pair in MBTI_CHEMISTRY.get("best", []) or rev_pair in MBTI_CHEMISTRY.get("best", []):
        return {"score": 100, "label_ko": "천생연분"}
    if pair in MBTI_CHEMISTRY.get("good", []) or rev_pair in MBTI_CHEMISTRY.get("good", []):
        return {"score": 85, "label_ko": "꿀케미"}
    if pair in MBTI_CHEMISTRY.get("bad", []) or rev_pair in MBTI_CHEMISTRY.get("bad", []):
        return {"score": 30, "label_ko": "아슬아슬"}
    
    return {"score": 60, "label_ko": "조화로운 케미"}


def get_idol_mbti_from_pool(name: str) -> str:
    """아이돌 풀에서 MBTI를 조회합니다. (부분 일치 지원)"""
    name_lower = name.lower().strip()
    for idol in IDOL_POOL:
        # 정확한 이름 또는 부분 일치 확인
        if (idol["name_kr"].lower() == name_lower or 
            idol["name_en"].lower().replace("-", " ") == name_lower or
            name_lower in idol["name_kr"].lower() or
            name_lower in idol["name_en"].lower()):
            return idol.get("mbti", "")
    return ""


@app.get("/api/idols/popular")
def get_popular_idols():
    """상단 남성 5명, 하단 여성 5명을 무작위로 추출하여 반환합니다."""
    pool = IDOL_POOL
    
    # 성별 필터링
    males = [i for i in pool if i.get("gender") == "male"]
    females = [i for i in pool if i.get("gender") == "female" or i.get("gender") is None] # 기본값 female
    
    # 오늘 날짜 기반 시드 설정 (매일 바뀜)
    today_str = datetime.now().strftime("%Y-%m-%d")
    seed_val = int(hashlib.md5(today_str.encode()).hexdigest(), 16)
    rng = random.Random(seed_val)
    
    # 각각 5명씩 추출
    selected_males = rng.sample(males, min(5, len(males)))
    selected_females = rng.sample(females, min(5, len(females)))
    
    def format_idol(idol, idx, gender):
        return {
            "id": f"{gender}_{idx}",
            "name_kr": idol["name_kr"],
            "name_en": idol["name_en"],
            "group": idol["group"],
            "gender": gender,
            "mbti": idol.get("mbti", ""),
            "birth_date": idol.get("birth_date", ""),
            "img_id": str((idx % 8) + 1) # 이미지 로테이션
        }

    data = {
        "male": [format_idol(i, idx, "male") for idx, i in enumerate(selected_males)],
        "female": [format_idol(i, idx, "female") for idx, i in enumerate(selected_females)]
    }
    
    return {"status": "success", "data": data}


@app.get("/api/idol/candidates")
def get_idol_candidates(name: str = Query(..., min_length=1)):
    """
    Wikipedia에서 이름과 일치하는 후보 목록을 반환합니다.
    복수의 후보가 있을 경우 프론트엔드에서 사용자에게 선택을 요청합니다.
    """
    print(f"🔍 [API] Candidates Request: {name}")
    try:
        from run_search import get_candidates
        candidates = get_candidates(name)
        return {"status": "success", "candidates": candidates}
    except Exception as e:
        print(f"❌ Candidates Error: {e}")
        return {"status": "success", "candidates": []}


@app.get("/api/idol/search")
def search_idol_info(
    name: str = Query(..., min_length=1),
    wiki_title: str = Query("", description="Confirmed Wikipedia page title"),
    wiki_lang: str = Query("en", description="Wikipedia language (en/ko)"),
):
    """
    아이돌 정보 검색.
    - wiki_title 없음: 일반 검색 (상위 후보 자동 선택)
    - wiki_title 있음: 사용자가 선택한 Wikipedia 항목으로 정확 조회
    """
    print(f"🚀 [API] Search: {name} | wiki_title={wiki_title}")

    # 1. wiki_title이 없을 경우, 먼저 IDOL_POOL에서 정확히 일치하는 데이터가 있는지 확인 (속도 최적화)
    if not wiki_title:
        pool_data = next((idol for idol in IDOL_POOL if idol["name_kr"] == name or idol["name_en"].lower() == name.lower()), None)
        if pool_data and pool_data.get("birth_date"):
            print(f"  ✨ Found in IDOL_POOL: {name}")
            # 데이터 형식을 검색 결과 형식에 맞게 변환
            return {
                "status": "success", 
                "data": {
                    "name": pool_data["name_kr"],
                    "birth_date": pool_data["birth_date"],
                    "gender": pool_data.get("gender", "female"),
                    "mbti": pool_data["mbti"]
                }
            }

    try:
        ai_result = search_idol_perplexity(name, wiki_title=wiki_title, wiki_lang=wiki_lang)

        if ai_result and ai_result.get("birth_date"):
            # MBTI가 비어있으면 아이돌 풀에서 폴백 조회
            if not ai_result.get("mbti"):
                ai_result["mbti"] = get_idol_mbti_from_pool(name)
            return {"status": "success", "data": ai_result}

        # 검색 결과가 없을 때도 아이돌 풀에서 MBTI 폴백 시도
        fallback_mbti = get_idol_mbti_from_pool(name)
        return {
            "status": "success", # 404 대신 success 반환 (브라우저 처리 용이)
            "is_manual": True,
            "message": f"Could not find verified data for {name}. Please enter manually.",
            "data": {
                "name": name,
                "birth_date": "",
                "gender": "female",
                "mbti": fallback_mbti
            }
        }
    except Exception as e:
        print(f"❌ API Error: {e}")
        return {"status": "error", "message": str(e), "data": None}

@app.get("/api/celebs")
def get_celebs_alias(search: Optional[str] = Query(None)):
    """Legacy alias for /api/idol/search"""
    if search:
        return search_idol_info(name=search)
    return get_popular_idols()

@app.get("/api/categories")
def get_categories_alias():
    """Legacy alias for categories"""
    return {"status": "success", "data": ["K-POP", "Actor", "Solo"]}

@app.get("/api/stats")
def get_stats():
    return {
        "status": "success",
        "data": {
            "today_challengers": STATS.get("today_challengers", 0),
            "total_visitors": STATS.get("total_visitors", 0)
        }
    }


@app.post("/api/stats/visit")
def record_visit(visitor_id: Optional[str] = Query(None)):
    """UV(Unique Visitor) 기반 방문자 기록"""
    if visitor_id and visitor_id not in STATS.get("voter_ids", []):
        STATS["total_visitors"] += 1
        if "voter_ids" not in STATS: STATS["voter_ids"] = []
        STATS["voter_ids"].append(visitor_id)
        save_stats()
        return {"status": "success", "data": STATS, "counted": True}
    return {"status": "success", "data": STATS, "counted": False}

@app.post("/api/stats/challenge")
def record_challenge():
    """실제 분석 완료 시 카운트 (도전자 수)"""
    STATS["today_challengers"] += 1
    save_stats()
    return {"status": "success", "data": STATS}


@app.get("/api/idol/assistant")
def assistant_search(name: str):
    """
    정규 데이터가 없을 때 구글/DuckDuckGo 스니펫 검색을 통해 생년월일과 MBTI를 유추해줍니다.
    """
    try:
        from run_search import get_assistant_info
        info = get_assistant_info(name)
        return {"status": "success", "data": info}
    except Exception as e:
        print(f"❌ Assistant API Error: {e}")
        return {"status": "error", "message": str(e), "data": {"birth_date": "", "mbti": ""}}

@app.get("/api/saju/analyze")
def analyze_saju(
    birth_date: str, 
    gender: str = "female",
    user_mbti: str = "",
    idol_name: str = "",
    idol_mbti: str = "",
    idol_birth_date: str = "",
    lang: str = "ko"
):
    print(f"🔮 [API] Analyze Saju: {birth_date} | {gender} | user_mbti={user_mbti} | idol={idol_name} | lang={lang}")
    try:
        from saju_engine import analyze_destiny
        result = analyze_destiny(birth_date, gender, user_mbti, idol_name, idol_mbti, idol_birth_date, lang)
        return {"status": "success", "analysis": result}
    except Exception as e:
        print(f"❌ [API] Analyze Error: {e}")
        return {"status": "error", "message": str(e)}


@app.get("/api/comments")
def get_comments():
    return {"status": "success", "comments": COMMENTS}

class PostCommentRequest(BaseModel):
    author: str
    content: str

@app.post("/api/comments")
def post_comment(req: PostCommentRequest):
    new_id = str(len(COMMENTS) + 1)
    new_comment = {
        "id": new_id,
        "author": req.author,
        "handle": f"@{req.author.lower().replace(' ', '_')}",
        "content": req.content,
        "timestamp": "Just now",
        "likes": 0,
        "avatar_color": f"#{random.randint(0, 0xFFFFFF):06x}",
        "replies": []
    }
    COMMENTS.insert(0, new_comment)
    return {"status": "success", "comment": new_comment}


@app.delete("/api/comments/{comment_id}")
def delete_comment(comment_id: str):
    global COMMENTS
    original_len = len(COMMENTS)
    COMMENTS = [c for c in COMMENTS if c["id"] != comment_id]
    
    if len(COMMENTS) < original_len:
        print(f"🗑️ Comment deleted: {comment_id}")
        return {"status": "success", "message": "Comment deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Comment not found")


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
