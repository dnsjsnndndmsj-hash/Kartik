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

            print("Trying to open Work Energy chapter...")
            await page.evaluate("physGoToChapter('phys-ch6-work-energy')")

            await asyncio.sleep(2)

            print("Taking screenshot...")
            await page.screenshot(path="verification_work_energy.png", full_page=True)
            print("Saved verification_work_energy.png")

            # Check for console errors
            page.on("console", lambda msg: print(f"Console {msg.type}: {msg.text}"))

        finally:
            server.terminate()
            await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
