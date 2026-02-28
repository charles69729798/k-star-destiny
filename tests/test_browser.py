import asyncio
from playwright.async_api import async_playwright
import sys

# Windows policy fix
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

async def test_browser():
    print("🚀 Testing Browser Launch...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://www.google.com")
        print("✅ Browser Launched! Keeping open for 5 seconds...")
        await asyncio.sleep(5)
        await browser.close()
        print("✅ Test Complete.")

if __name__ == "__main__":
    asyncio.run(test_browser())
