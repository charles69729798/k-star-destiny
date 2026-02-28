import json
import os

with open("saju_i18n.py", "r", encoding="utf-8") as f:
    content = f.read()

# Define SYNERGY_MISSIONS data
synergy_missions = {
    "ko": {
        "vibe": {
            "label": "갓벽한 무드 공유 📸",
            "boost": 12,
            "reason": "서로의 취향을 공유하며 주파수를 맞춥니다.",
            "tasks": ["오늘의 추천곡 링크 보내기", "인생네컷 포즈 정해보기", "최애 카페 리스트 공유"]
        },
        "heart": {
            "label": "딥다이브 진심 토크 💬",
            "boost": 18,
            "reason": "깊은 대화는 보이지 않는 연결고리를 단단하게 합니다.",
            "tasks": ["서로의 MBTI T/F 모먼트 말하기", "힘들 때 듣고 싶은 말 고르기", "1년 뒤 우리에게 편지 쓰기"]
        },
        "energy": {
            "label": "도파민 힐링 데이트 🎡",
            "boost": 20,
            "reason": "함께 새로운 경험을 하며 에너지를 증폭시킵니다.",
            "tasks": ["안 가본 동네에서 맛집 탐방", "서로의 퍼스널 컬러 진단해주기", "함께 일몰 보며 멍 때리기"]
        }
    },
    "en": {
        "vibe": {
            "label": "Perfect Vibe Sharing 📸",
            "boost": 12,
            "reason": "Syncing frequencies by sharing each other's tastes.",
            "tasks": ["Send link to Today's Recommendation song", "Decide on a Pose for Photo Booth", "Share list of Favorite Cafes"]
        },
        "heart": {
            "label": "Deep Dive Sincere Talk 💬",
            "boost": 18,
            "reason": "Deep conversations strengthen the invisible connection.",
            "tasks": ["Tell each other's MBTI T/F moments", "Pick words you want to hear when tired", "Write a letter to 'Us' 1 year later"]
        },
        "energy": {
            "label": "Dopamine Healing Date 🎡",
            "boost": 20,
            "reason": "Amplifying energy by experiencing new things together.",
            "tasks": ["Explore famous restaurants in new town", "Diagnose each other's Personal Color", "Stare into space while watching sunset"]
        }
    }
}

# Add ES and PT based on EN
synergy_missions["es"] = {
    "vibe": {
        "label": "Compartir Vibras Perfectas 📸",
        "boost": 12,
        "reason": "Sincronizando frecuencias compartiendo gustos.",
        "tasks": ["Enviar link de Canción Recomendada", "Decidir Pose para el Photo Booth", "Compartir lista de Cafeterías Favoritas"]
    },
    "heart": {
        "label": "Charla Sincera Profunda 💬",
        "boost": 18,
        "reason": "Las conversaciones profundas fortalecen la conexión.",
        "tasks": ["Contar momentos MBTI T/F", "Elegir palabras de apoyo", "Escribir una carta al 'Nosotros' futuro"]
    },
    "energy": {
        "label": "Cita de Sanación y Dopamina 🎡",
        "boost": 20,
        "reason": "Amplificando la energía con nuevas experiencias.",
        "tasks": ["Explorar restaurantes en zona nueva", "Diagnóstico de Color Personal", "Mirar el atardecer juntos"]
    }
}

synergy_missions["pt"] = {
    "vibe": {
        "label": "Compartilhar Vibes Perfeitas 📸",
        "boost": 12,
        "reason": "Sincronizando frequências ao compartilhar gostos.",
        "tasks": ["Enviar link da Música Recomendada", "Decidir Pose para o Photo Booth", "Compartilhar lista de Cafés Favoritos"]
    },
    "heart": {
        "label": "Papo Sincero Profundo 💬",
        "boost": 18,
        "reason": "Conversas profundas fortalecem a conexão invisível.",
        "tasks": ["Contar momentos MBTI T/F", "Escolher palavras de conforto", "Escrever carta para 'Nós' daqui a 1 ano"]
    },
    "energy": {
        "label": "Encontro de Cura e Dopamina 🎡",
        "boost": 20,
        "reason": "Amplificando a energia com novas experiências junots.",
        "tasks": ["Explorar novos bares e restaurantes", "Diagnóstico de Cor Pessoal", "Ver o pôr do sol sem fazer nada"]
    }
}

# Inject into I18N_DATA
# This script assumes I18N_DATA is a dict in saju_i18n.py
# We will use a more robust way to inject: 
# Find the end of each language's dict and insert SYNERGY_MISSIONS

import re

for lang in ["en", "ko", "es", "pt"]:
    pattern = rf'"{lang}": \{{'
    match = re.search(pattern, content)
    if match:
        # Find the closing brace for this language
        # We'll use a simple count of braces
        start = match.end()
        count = 1
        i = start
        while count > 0 and i < len(content):
            if content[i] == '{': count += 1
            elif content[i] == '}': count -= 1
            i += 1
        
        # Insert SYNERGY_MISSIONS before the closing brace '}'
        # i is now the index after '}'
        insertion_point = i - 1
        
        # Format the missions data for injection
        missions_json = json.dumps(synergy_missions[lang], indent=8, ensure_ascii=False)
        # Remove leading/trailing braces of the json dump to merge
        # missions_json = missions_json.strip()
        
        injection = f',\n        "SYNERGY_MISSIONS": {missions_json}'
        content = content[:insertion_point] + injection + content[insertion_point:]

with open("saju_i18n.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully injected SYNERGY_MISSIONS into saju_i18n.py for all languages.")
