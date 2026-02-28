import asyncio
from playwright.async_api import async_playwright
import os

# 테스트할 인물 10명
TARGETS = [
    "박보검", "아이유", "정국", "카리나", "장원영",
    "차은우", "제니", "손흥민", "유재석", "김연아"
]

async def run_virtual_user(name, idx):
    print(f"👤 [User {idx}] '{name}' 검색 시작...")
    
    async with async_playwright() as p:
        # 가상 사용자 브라우저 실행 (Headless 모드로 빠르게)
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1280, "height": 800})
        page = await context.new_page()

        try:
            # 1. 웹사이트 접속
            await page.goto("http://localhost:5173")
            await page.wait_for_load_state("networkidle")
            
            # 2. 검색어 입력
            await page.fill('input[placeholder*="Idol Name"]', name)
            
            # 3. AI MODE 버튼 클릭
            # 버튼 텍스트가 "AI MODE" 또는 "AI 모드"일 수 있음
            await page.click('button:has-text("AI MODE"), button:has-text("AI 모드")')
            
            # 4. 로딩 대기 (최대 60초)
            print(f"   ⏳ [User {idx}] AI 검색 중... (대기)")
            
            # 성공 케이스: 결과 카드가 떴을 때 (프로필 이름이 보일 때)
            # 실패 케이스: "ERROR" 메시지가 떴을 때
            try:
                # 둘 중 하나가 뜰 때까지 대기
                await page.wait_for_selector('h3.text-3xl, .bg-red-500\/10', timeout=60000)
            except:
                print(f"   ❌ [User {idx}] 타임아웃! 결과가 안 뜸.")
                await page.screenshot(path=f"test_results/user_{idx}_{name}_timeout.png")
                return

            # 5. 결과 확인 및 스크린샷
            # 에러 메시지가 있는지 확인
            if await page.locator('.bg-red-500\/10').count() > 0:
                print(f"   ❌ [User {idx}] 검색 실패 (에러 메시지 뜸)")
                await page.screenshot(path=f"test_results/user_{idx}_{name}_fail.png")
            else:
                # 생년월일 데이터 확인
                birth_date = await page.input_value('input[placeholder="YYYY-MM-DD"]') if await page.is_visible('input[placeholder="YYYY-MM-DD"]') else await page.inner_text('div.flex-1 p.text-xl')
                print(f"   ✅ [User {idx}] 성공! 생년월일: {birth_date}")
                await page.screenshot(path=f"test_results/user_{idx}_{name}_success.png")

        except Exception as e:
            print(f"   ⚠️ [User {idx}] 에러 발생: {e}")
            await page.screenshot(path=f"test_results/user_{idx}_{name}_error.png")
        finally:
            await browser.close()

async def main():
    # 결과 폴더 생성
    if not os.path.exists("test_results"):
        os.makedirs("test_results")
        
    print("🚀 가상 사용자 10명 테스트 시작 (순차 실행)...")
    
    # 순차적으로 실행 (서버 부하 고려)
    for i, name in enumerate(TARGETS):
        await run_virtual_user(name, i+1)
        print("-" * 40)

if __name__ == "__main__":
    asyncio.run(main())
