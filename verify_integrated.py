import asyncio
from playwright.async_api import async_playwright
import time

async def verify_integrated_gui():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Connect to the Flask server
        await page.goto("http://localhost:5000")
        await page.wait_for_timeout(1000)

        # Send a command
        await page.get_by_placeholder("Give a command...").fill("list files")
        await page.keyboard.press("Enter")
        await page.wait_for_timeout(2000) # Wait for backend response

        # Take a screenshot
        await page.screenshot(path="jarvis_integrated_screenshot.png")

        content = await page.content()
        if "DESIGN.md" in content:
            print("Integrated GUI Verification: Successfully received backend response.")
        else:
            print("Integrated GUI Verification: Failed to receive expected backend response.")

        await browser.close()

if __name__ == "__main__":
    time.sleep(2) # Give server time to start
    asyncio.run(verify_integrated_gui())
