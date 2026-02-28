from playwright.sync_api import sync_playwright
import time
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

name = sys.argv[1] if len(sys.argv) > 1 else "장원영"
query = f"{name} 생년월일 MBTI"

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=True,
        args=['--no-sandbox','--disable-blink-features=AutomationControlled','--lang=ko-KR']
    )
    context = browser.new_context(
        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        locale='ko-KR',
        timezone_id='Asia/Seoul',
        viewport={'width': 1280, 'height': 800}
    )
    context.add_init_script("Object.defineProperty(navigator, 'webdriver', { get: () => undefined })")
    page = context.new_page()
    
    # 1. Google 홈 접속
    page.goto('https://www.google.co.kr/?hl=ko', timeout=20000)
    time.sleep(2)
    
    # 2. 동의 버튼 처리
    try:
        for selector in ['#L2AGLb', 'button:has-text("동의")', 'button:has-text("Accept all")']:
            btn = page.query_selector(selector)
            if btn:
                btn.click()
                time.sleep(1)
                break
    except:
        pass
    
    # 3. 검색창 찾아서 타이핑
    search_box = page.wait_for_selector('textarea[name="q"], input[name="q"]', timeout=8000)
    search_box.click()
    time.sleep(0.5)
    search_box.type(query, delay=60)
    time.sleep(1)
    page.keyboard.press("Enter")
    
    # 4. 검색 결과 기다리기
    try:
        page.wait_for_selector('#search', timeout=15000)
    except:
        pass
    time.sleep(2)
    
    page.screenshot(path='debug_search_result.png')
    content = page.content()
    print(f"Result page len: {len(content)}", file=sys.stderr)
    print(f"URL: {page.url}", file=sys.stderr)
    
    # 5. 내용 출력
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')
    text = soup.get_text(separator=' ')
    print(text[:2000], file=sys.stderr)
    
    browser.close()
