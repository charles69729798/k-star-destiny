import puppeteer from 'puppeteer';

(async () => {
  const browser = await puppeteer.launch({ headless: "new" });
  const page = await browser.newPage();
  
  try {
    // Navigate to the frontend (using the last known port 5177)
    await page.goto('http://localhost:5177', { waitUntil: 'networkidle0' });
    
    // Set viewport to standard desktop size
    await page.setViewport({ width: 1280, height: 800 });

    // Take screenshot
    await page.screenshot({ path: 'current-screen.png' });
    console.log('Screenshot captured: current-screen.png');

  } catch (error) {
    console.error('Error capturing screen:', error);
  } finally {
    await browser.close();
  }
})();