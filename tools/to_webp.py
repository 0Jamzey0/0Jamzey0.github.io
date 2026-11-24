import os, glob
from PIL import Image
before = after = 0
for p in glob.glob("img/**/*.jpg", recursive=True) + glob.glob("img/**/*.png", recursive=True):
    n = os.path.basename(p)
    if n in ("social.jpg", "card.jpg"): continue   # og:image must stay JPG
    im = Image.open(p)
    out = os.path.splitext(p)[0] + ".webp"
    if p.endswith(".png"):
        im.save(out, "WEBP", quality=88, method=6)   # keeps alpha (mark, logo)
    else:
        im.convert("RGB").save(out, "WEBP", quality=76, method=6)
    before += os.path.getsize(p); after += os.path.getsize(out)
print(before//1024, "KB ->", after//1024, "KB")
