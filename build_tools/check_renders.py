import os
from PIL import Image

render_files = sorted(os.listdir('test_renders'))
print(f"Total render snapshots: {len(render_files)}")

for f in render_files:
    if f.endswith('.png'):
        p = os.path.join('test_renders', f)
        im = Image.open(p)
        bbox = im.getbbox()
        print(f"{f}: size={im.size}, non-empty bbox={bbox}")
