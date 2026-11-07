from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(channel="msedge", headless=True)
    page = browser.new_page()
    page.set_content("<html><body><h1>Playwright with Edge Works!</h1></body></html>")
    page.screenshot(path="test_playwright.png")
    browser.close()
    print("Screenshot taken successfully!")
