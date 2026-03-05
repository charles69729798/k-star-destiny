import requests
import json

def test_analyze():
    url = "http://localhost:8000/api/saju/analyze"
    params = {
        "birth_date": "1990-01-01",
        "gender": "female",
        "user_mbti": "INFJ",
        "idol_name": "Karina",
        "idol_mbti": "ENFP",
        "idol_birth_date": "2000-04-11",
        "lang": "ko"
    }
    try:
        response = requests.get(url, params=params)
        print(f"Status Code: {response.status_code}")
        data = response.json()
        print(f"Total Response Size: {len(response.text)} bytes")
        if "analysis" in data:
            fortune = data["analysis"].get("monthly_fortune", [])
            print(f"Monthly Fortune Count: {len(fortune)}")
            if len(fortune) > 0:
                print("First month sample:")
                print(json.dumps(fortune[0], indent=2, ensure_ascii=False))
        else:
            print("Error: 'analysis' key not found in response")
            print(data)
    except Exception as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    test_analyze()
