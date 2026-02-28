from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=True,
        args=['--no-sandbox','--disable-blink-features=AutomationControlled','--lang=ko-KR']
    )
    context = browser.new_context(
        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        locale='ko-KR',
        timezone_id='Asia/Seoul'
    )
    context.add_init_script("Object.defineProperty(navigator, 'webdriver', { get: () => undefined })")
    page = context.new_page()
    page.goto('https://www.google.co.kr/?hl=ko', timeout=20000)
    time.sleep(2)
    page.screenshot(path='debug_google.png')
    print('title:', page.title())
    print('url:', page.url)
    print('len:', len(page.content()))
    # 페이지의 처음 500자 출력
    print('content_preview:', page.content()[:500])
    browser.close()
