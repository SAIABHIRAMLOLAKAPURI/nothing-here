import asyncio
from playwright.async_api import async_playwright
import os

async def verify_gui():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        # Load the local index.html
        path = os.path.abspath("jarvis/interface/index.html")
        await page.goto(f"file://{path}")

        # Take a screenshot
        await page.screenshot(path="jarvis_gui_screenshot.png")
        print("Screenshot saved to jarvis_gui_screenshot.png")

        # Verify JARVIS is present
        content = await page.content()
        if "JARVIS" in content:
            print("GUI Verification: JARVIS found in page content.")
        else:
            print("GUI Verification: JARVIS NOT found in page content.")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify_gui())
