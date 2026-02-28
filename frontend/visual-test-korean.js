import puppeteer from 'puppeteer';

const testCases = [
  { name: '아이유', expect: 'auto' },
  { name: '정국', expect: 'auto' },
  { name: '지민', expect: 'auto' }, // New test for real search
  { name: '민지', expect: 'auto' }, // New test for real search
  { name: '카리나', expect: 'auto' },
  // Date Validation Tests (using manual entry fallback or direct input)
  { name: '테스트유저1', type: 'manual_test', dateInput: '20230230', expectInvalid: true }, // Invalid Day
  { name: '테스트유저2', type: 'manual_test', dateInput: '19901301', expectInvalid: true }, // Invalid Month
  { name: '테스트유저3', type: 'manual_test', dateInput: '21010101', expectInvalid: true }, // Invalid Year
  { name: '하니', expect: 'auto' },
  { name: '장원영', expect: 'auto' }
];

(async () => {
  console.log('🚀 Starting Visual Test (Real AI Search & Date Validation)...');
  const browser = await puppeteer.launch({ headless: "new" });
  const page = await browser.newPage();
  
  await page.setViewport({ width: 1280, height: 1200 });

  try {
    console.log('Connecting to localhost:5178...');
    await page.goto('http://localhost:5178', { waitUntil: 'networkidle0' });
    
    // 1. Switch to Korean
    const koBtn = await page.waitForSelector('button ::-p-text(KO)');
    if (koBtn) {
        await koBtn.click();
        console.log('✅ Switched to Korean Mode');
        await new Promise(r => setTimeout(r, 500));
    }

    // 2. Iterate through test cases
    for (let i = 0; i < testCases.length; i++) {
        const test = testCases[i];
        console.log(`\n[${i+1}/10] Testing: ${test.name}`);

        if (test.type === 'manual_test') {
            // Manual Test: Toggle Manual Mode and Test Date Input
            // We use the "Edit Manually" button (pencil icon) if available, or just use the user profile date input
            // Let's use the User Profile Date Input for validation testing as it's always visible
            const dateInput = await page.$('input[placeholder="YYYY-MM-DD"]'); // The first one is user profile
            
            // Clear input
            await page.evaluate((el) => el.value = '', dateInput);
            
            // Type the invalid date (raw numbers)
            await dateInput.type(test.dateInput);
            
            // Check if it has red border class
            const isInvalid = await page.evaluate((el) => el.classList.contains('border-red-500'), dateInput);
            
            if (isInvalid === test.expectInvalid) {
                console.log(`✅ Date Validation Passed for ${test.dateInput} (Invalid: ${isInvalid})`);
            } else {
                console.error(`❌ Date Validation Failed for ${test.dateInput}. Expected Invalid: ${test.expectInvalid}, Got: ${isInvalid}`);
            }
            
            await page.screenshot({ path: `test-date-${test.name}.png` });

        } else {
            // AI Search Test
            const inputSelector = 'input[placeholder*="아이돌 이름"]';
            await page.waitForSelector(inputSelector);
            
            await page.evaluate((sel) => { document.querySelector(sel).value = '' }, inputSelector);
            await page.type(inputSelector, test.name);

            const searchBtn = await page.$('form button[type="submit"]');
            await searchBtn.click();

            // Wait longer for real Google Search (it might take a few seconds)
            console.log('   Waiting for AI Search...');
            try {
                // Wait for either result card (bg-slate-800) or error message
                await page.waitForSelector('.bg-slate-800', { timeout: 10000 }); 
            } catch (e) {
                console.log('   Timeout waiting for result.');
            }
            
            // Check success state
            const isSuccess = await page.evaluate(() => {
                return !document.body.innerText.includes('데이터를 찾을 수 없습니다') && 
                       !document.body.innerText.includes('AI-Assisted Manual Mode');
            });

            if (isSuccess) {
                console.log(`✅ AI Search Success: Found data for ${test.name}`);
            } else {
                console.log(`⚠️ AI Search Fallback: Manual Mode triggered for ${test.name}`);
            }
            
            await page.screenshot({ path: `test-result-${i+1}-${test.name}.png` });
        }
    }

    console.log('\n✨ All tests completed.');

  } catch (error) {
    console.error('Test failed:', error);
  } finally {
    await browser.close();
  }
})();