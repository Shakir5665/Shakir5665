from PIL import Image

for name in ['id.png', 'right_pointing.png']:
    try:
        im = Image.open(name)
        print(f"{name}: mode={im.mode}, size={im.size}, format={im.format}")
        # check alpha channel
        if im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info):
            extrema = im.getextrema()
            print(f"  alpha channel present. alpha extrema: {extrema[-1] if im.mode == 'RGBA' else 'N/A'}")
        else:
            print("  no alpha channel")
    except Exception as e:
        print(f"Error checking {name}: {e}")
