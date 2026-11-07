from PIL import Image
import os

images = [
    'hero_as_img_desktop.png',
    'about-life_as_img_desktop.png',
    'stack_as_img_desktop.png',
    'id-dashboard_as_img_desktop.png',
    'connect_as_img_desktop.png'
]

for img_name in images:
    p = os.path.join('test_renders', img_name)
    if os.path.exists(p):
        im = Image.open(p)
        print(f"{img_name}: {im.size}")
