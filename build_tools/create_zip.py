import zipfile
import os

zip_filename = "profile-assets.zip"

files_to_pack = [
    "README.md",
    "preview.html",
    "id.png",
    "right_pointing.png",
    "assets/hero.svg",
    "assets/about-life.svg",
    "assets/stack.svg",
    "assets/id-dashboard.svg",
    "assets/connect.svg",
    "assets/fonts/LICENSE.txt"
]

with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for f in files_to_pack:
        if os.path.exists(f):
            zipf.write(f, arcname=f)
            print(f"Added {f} ({os.path.getsize(f):,} bytes)")
        else:
            print(f"WARNING: File {f} does not exist!")

print(f"\n{zip_filename} successfully created! Total archive size: {os.path.getsize(zip_filename):,} bytes")
