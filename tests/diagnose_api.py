import httpx
import asyncio
import time

async def test_api():
    url = "http://localhost:8000/api/idol/search"
    params = {"name": "박보검"}
    print(f"📡 [진단] API 요청 시작: {url} ? name=박보검")
    
    start_time = time.time()
    try:
        # 타임아웃을 60초로 넉넉하게 줌
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.get(url, params=params)
            
        duration = time.time() - start_time
        print(f"⏱ 소요 시간: {duration:.2f}초")
        
        if response.status_code == 200:
            print("✅ [성공] 서버 응답:")
            print(response.json())
        else:
            print(f"❌ [실패] 상태 코드: {response.status_code}")
            print(response.text)
            
    except httpx.RequestError as e:
        print(f"❌ [네트워크 에러] 연결 실패: {e}")
        print("   -> 백엔드 서버가 꺼져있거나 포트(8000)가 막혀있을 수 있습니다.")
    except httpx.TimeoutException:
        print("❌ [타임아웃] 60초 동안 응답이 없습니다.")

if __name__ == "__main__":
    asyncio.run(test_api())
