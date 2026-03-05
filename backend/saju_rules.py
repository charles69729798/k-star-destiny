# K-Destiny AI Business Rules & Logic Constants
# 이 파일은 사주/MBTI 분석에 사용되는 핵심 수치, 점수, 매핑 룰을 정의합니다.

# 1. MBTI 간 시너지 추가 점수 매핑
MBTI_CHEMISTRY = {
    "ENFJ": {"INFP": 20, "ISFP": 15}, 
    "INFP": {"ENFJ": 20, "ENTJ": 20}, 
    "ENTJ": {"INFP": 20, "ISFP": 15}, 
    "ISFP": {"ENFJ": 20, "ENTJ": 15}
}

# 2. 오행 상생(相生) 매핑 (A가 B를 낳음/도움)
ELEMENT_CREATION_MAP = {
    "Wood": "Fire",   # 목생화
    "Fire": "Earth",  # 화생토
    "Earth": "Metal", # 토생금
    "Metal": "Water", # 금생수
    "Water": "Wood"   # 수생목
}

# 3. 관계별 기본 시너지 점수 범위
SYNERGY_SCORE_RANGES = {
    "CREATE": (88, 98),   # 상생 관계
    "HARMONY": (82, 92),  # 같은 오행 (비견/겁재)
    "CONTROL": (68, 85)   # 상극 관계
}
