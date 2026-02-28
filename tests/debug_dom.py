import asyncio
from playwright.async_api import async_playwright
import os

async def debug_perplexity_dom():
    print("📸 [DEBUG] Perplexity DOM 진단 시작...")
    
    # "박보검" 테스트
    name = "박보검"
    prompt = f"What is the birth date (YYYY-MM-DD) and MBTI of {name}? Only provide verified information."
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False) # 사용자님도 보실 수 있게
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            locale="en-US",
            viewport={"width": 1280, "height": 800}
        )
        page = await context.new_page()

        try:
            # 1. 접속
            print("1. 접속 중...")
            await page.goto("https://www.perplexity.ai/", timeout=30000)
            await asyncio.sleep(2)
            await page.screenshot(path="debug_step1_main.png")
            print("   📸 step1_main.png 저장")

            # 2. 입력창 확인 및 입력
            print("2. 입력창 찾는 중...")
            # DOM 확인용: textarea 존재 여부
            if await page.locator("textarea").count() > 0:
                print("   ✅ textarea 발견됨")
                await page.fill("textarea", prompt)
                await page.screenshot(path="debug_step2_typing.png")
                print("   📸 step2_typing.png 저장")
                await page.keyboard.press("Enter")
            else:
                print("   ❌ textarea 없음! DOM 구조가 변경되었거나 로딩 실패.")
                # 현재 HTML 저장
                with open("debug_fail_dom.html", "w", encoding="utf-8") as f:
                    f.write(await page.content())
                return

            # 3. 답변 대기
            print("3. 답변 생성 대기 중 (10초)...")
            await asyncio.sleep(10)
            await page.screenshot(path="debug_step3_waiting.png")
            print("   📸 step3_waiting.png 저장")

            # 4. 결과 확인
            print("4. 결과 DOM 확인...")
            # 답변 영역(.prose)이 있는지 확인
            prose_count = await page.locator(".prose, .default-prose").count()
            if prose_count > 0:
                print(f"   ✅ 답변 영역(.prose) {prose_count}개 발견됨")
                text = await page.locator(".prose, .default-prose").first.inner_text()
                print(f"   📜 추출된 텍스트(일부): {text[:100]}...")
                await page.screenshot(path="debug_step4_success.png")
            else:
                print("   ❌ 답변 영역(.prose)을 찾을 수 없음!")
                await page.screenshot(path="debug_step4_fail.png")
                
        except Exception as e:
            print(f"❌ 에러 발생: {e}")
            await page.screenshot(path="debug_error.png")
        finally:
            await browser.close()
            print("🏁 진단 종료")

if __name__ == "__main__":
    asyncio.run(debug_perplexity_dom())
