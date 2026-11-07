import os
from playwright.sync_api import sync_playwright

abs_dir = os.path.abspath('.').replace('\\', '/')

html = f"""
<!DOCTYPE html>
<html>
<body style="background: #0d1117; margin: 0; padding: 20px;">
  <div style="width: 880px;">
    <img id="img1" src="assets/hero.svg" style="width: 100%; height: auto; display: block;" />
  </div>
</body>
</html>
"""

test_html_path = os.path.abspath('test_page.html').replace('\\', '/')
with open(test_html_path, 'w', encoding='utf-8') as f:
    f.write(html)

with sync_playwright() as p:
    browser = p.chromium.launch(channel="msedge", headless=True)
    page = browser.new_page(viewport={"width": 1000, "height": 800})
    page.goto(f"file:///{test_html_path}")
    page.wait_for_timeout(500)
    box = page.locator("#img1").bounding_box()
    print("Bounding box when loaded from file:// URL:", box)
    page.screenshot(path="test_renders/real_img_render.png")
    browser.close()
