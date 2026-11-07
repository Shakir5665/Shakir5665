from PIL import Image

for name in ['id.png', 'right_pointing.png']:
    im = Image.open(name)
    bbox = im.getbbox()
    print(f"{name}: size={im.size}, non-zero bbox={bbox}")
