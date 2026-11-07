from playwright.sync_api import sync_playwright
import os

abs_svg = os.path.abspath('assets/id-dashboard.svg').replace('\\', '/')

with sync_playwright() as p:
    browser = p.chromium.launch(channel="msedge", headless=True)
    page = browser.new_page()
    
    logs = []
    page.on("console", lambda msg: logs.append(f"CONSOLE: {msg.type}: {msg.text}"))
    page.on("pageerror", lambda err: logs.append(f"PAGEERROR: {err}"))
    
    page.goto(f"file:///{abs_svg}")
    page.wait_for_timeout(500)
    
    # Check if svg is parsed
    title = page.title()
    svg_box = page.locator("svg").bounding_box()
    print("Page title:", title)
    print("SVG bounding box directly:", svg_box)
    print("Logs:", logs)
    
    # Now check as img
    temp_html = f"""<!DOCTYPE html><html><body><img id="testimg" src="file:///{abs_svg}" style="width: 880px;" /></body></html>"""
    page.set_content(temp_html)
    page.wait_for_timeout(500)
    img_box = page.locator("#testimg").bounding_box()
    print("IMG bounding box:", img_box)
    
    browser.close()
