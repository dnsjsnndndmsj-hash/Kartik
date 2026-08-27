import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # We need a local server running
        print("Starting server...")
        import subprocess
        server = subprocess.Popen(['python3', '-m', 'http.server', '8000'])

        try:
            await asyncio.sleep(2) # Give server time to start
            print("Navigating to page...")
            await page.goto("http://localhost:8000/index.html")

            print("Bypassing lock screen...")
            await page.evaluate("""() => {
                document.getElementById('lockScreen').style.display = 'none';
                document.getElementById('profileGateScreen').style.display = 'none';
                switchView('dashboard');
            }""")

            # Wait a moment
            await asyncio.sleep(1)

            print("Switching to NCERT MCQs...")
            await page.evaluate("switchView('ncert-mcq')")
            await asyncio.sleep(1)

            print("Taking screenshot of MCQ selection...")
            await page.screenshot(path="verification_mcq_list.png", full_page=True)

            print("Starting Bio MCQ...")
            await page.evaluate("startMcqSession('bio-ch8')")
            await asyncio.sleep(1)

            print("Taking screenshot of MCQ active session...")
            await page.screenshot(path="verification_mcq_active.png", full_page=True)

        finally:
            server.terminate()
            await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
