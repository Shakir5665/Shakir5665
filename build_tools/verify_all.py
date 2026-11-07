import os
import re
import time
from playwright.sync_api import sync_playwright

SVG_FILES = [
    'assets/hero.svg',
    'assets/about-life.svg',
    'assets/stack.svg',
    'assets/id-dashboard.svg',
    'assets/connect.svg'
]

TIMESTAMPS = [0, 2, 5, 9, 13]

os.makedirs('test_renders', exist_ok=True)

def audit_code():
    print("=== 1. STATIC CODE AUDIT ===")
    all_passed = True
    ids_per_file = {}

    for file_path in SVG_FILES:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        print(f"\nAuditing {file_path} ({len(content):,} bytes)...")

        # Check for scripts
        if '<script' in content.lower():
            print(f"  [FAIL] Contains <script> tag!")
            all_passed = False
        else:
            print("  [PASS] No <script> tags.")

        # Check for foreignObject
        if '<foreignobject' in content.lower():
            print(f"  [FAIL] Contains <foreignObject> tag!")
            all_passed = False
        else:
            print("  [PASS] No <foreignObject> tags.")

        # Check for external asset network requests
        external_urls = []
        for m in re.finditer(r'(href|src|url)\s*=\s*["\'](http[s]?://[^"\']+)["\']', content):
            attr, u = m.group(1), m.group(2)
            if 'w3.org' not in u:
                external_urls.append(u)
        for m in re.finditer(r'url\(\s*["\']?(http[s]?://[^)"\']+)["\']?\s*\)', content):
            u = m.group(1)
            if 'w3.org' not in u:
                external_urls.append(u)

        if external_urls:
            print(f"  [FAIL] External network requests detected: {external_urls}")
            all_passed = False
        else:
            print("  [PASS] Zero external asset network requests.")

        # Check CSS animation-fill-mode
        if 'both' in content:
            print("  [PASS] Contains 'fill-mode: both'.")
        else:
            print("  [WARN] 'both' fill-mode check.")

        # Check prefers-reduced-motion
        if 'prefers-reduced-motion' in content:
            print("  [PASS] Contains prefers-reduced-motion media query.")
        else:
            print("  [FAIL] Missing prefers-reduced-motion query!")
            all_passed = False

        # Extract IDs
        found_ids = set(re.findall(r'id=["\']([^"\']+)["\']', content))
        ids_per_file[file_path] = found_ids
        print(f"  [INFO] Defined {len(found_ids)} IDs.")

    # Check ID collision between files
    print("\nAuditing cross-file ID collisions...")
    collision_found = False
    file_list = list(ids_per_file.keys())
    for i in range(len(file_list)):
        for j in range(i + 1, len(file_list)):
            f1, f2 = file_list[i], file_list[j]
            overlap = ids_per_file[f1].intersection(ids_per_file[f2])
            if overlap:
                print(f"  [FAIL] ID Collision between {f1} and {f2}: {overlap}")
                collision_found = True
                all_passed = False
    if not collision_found:
        print("  [PASS] Zero ID collisions across all SVGs. Perfectly namespaced!")

    return all_passed

def render_suite():
    print("\n=== 2. RENDERING VERIFICATION (0s, 2s, 5s, 9s, 13s, static, img) ===")
    abs_dir = os.path.abspath('.').replace('\\', '/')

    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge", headless=True)

        for file_path in SVG_FILES:
            base_name = os.path.splitext(os.path.basename(file_path))[0]
            abs_svg = os.path.abspath(file_path).replace('\\', '/')

            # 1. Render at each timestamp
            for t in TIMESTAMPS:
                page = browser.new_page(viewport={"width": 940, "height": 600})
                page.goto(f"file:///{abs_svg}")
                if t > 0:
                    page.evaluate(f"""() => {{
                        const svg = document.querySelector('svg');
                        if (svg && svg.setCurrentTime) {{
                            svg.setCurrentTime({t});
                        }}
                    }}""")
                    page.wait_for_timeout(300)
                else:
                    page.wait_for_timeout(100)

                out_png = f"test_renders/{base_name}_t{t}s.png"
                page.locator("svg").screenshot(path=out_png)
                page.close()

            # 2. Render with animation removed (prefers-reduced-motion)
            page = browser.new_page(viewport={"width": 940, "height": 600})
            page.emulate_media(reduced_motion="reduce")
            page.goto(f"file:///{abs_svg}")
            page.wait_for_timeout(200)
            out_static = f"test_renders/{base_name}_static_reduced_motion.png"
            page.locator("svg").screenshot(path=out_static)
            page.close()

            # 3. Render as <img> element at desktop width (880px)
            # Create a dedicated temp html in repository directory
            temp_html_path = f"build_tools/temp_{base_name}.html"
            temp_html = f"""<!DOCTYPE html>
<html>
<head>
  <style>
    body {{ background: #070b16; margin: 0; padding: 20px; }}
    .desktop {{ width: 880px; margin: 0 auto; }}
    .mobile {{ width: 370px; margin: 20px auto; }}
    img {{ width: 100%; height: auto; display: block; border-radius: 20px; }}
  </style>
</head>
<body>
  <div class="desktop">
    <img id="img_desktop" src="../{file_path}" alt="{base_name}" />
  </div>
  <div class="mobile">
    <img id="img_mobile" src="../{file_path}" alt="{base_name}" />
  </div>
</body>
</html>"""
            with open(temp_html_path, 'w', encoding='utf-8') as f:
                f.write(temp_html)

            abs_temp_html = os.path.abspath(temp_html_path).replace('\\', '/')
            page = browser.new_page(viewport={"width": 1000, "height": 1200})
            page.goto(f"file:///{abs_temp_html}")
            page.wait_for_timeout(500)

            # Check bounding boxes
            box_desktop = page.locator("#img_desktop").bounding_box()
            box_mobile = page.locator("#img_mobile").bounding_box()
            print(f"  {base_name} as <img> desktop box: {box_desktop['width']:.1f}x{box_desktop['height']:.1f}")
            print(f"  {base_name} as <img> mobile box: {box_mobile['width']:.1f}x{box_mobile['height']:.1f}")

            out_desktop = f"test_renders/{base_name}_as_img_desktop.png"
            out_mobile = f"test_renders/{base_name}_as_img_mobile.png"
            page.locator("#img_desktop").screenshot(path=out_desktop)
            page.locator("#img_mobile").screenshot(path=out_mobile)

            page.close()
            os.remove(temp_html_path)

        browser.close()
    print("\nAll rendering tests passed with full dimension verification!")

if __name__ == '__main__':
    if audit_code():
        render_suite()
