"""Converts the P_Zenos screenshots into site images. Run when the shots change:
python tools/prepare_zenos.py
Shots are numbered 00, 01, ... in filename order; build.py refers to them by that number.
"""
import glob, os
from PIL import Image

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHOTS = "F:/P_ZeonVer1/Screenshots"
OUT = os.path.join(SITE, "img", "pzenos")
CARD = 19   # shot used for the link-preview card

def fit(im, width):
    return im.resize((width, round(im.height * width / im.width)), Image.LANCZOS) if im.width > width else im

os.makedirs(OUT, exist_ok=True)
src = sorted(glob.glob(f"{SHOTS}/*.png") + glob.glob(f"{SHOTS}/*.jpg"))
total = 0
for i, p in enumerate(src):
    im = Image.open(p).convert("RGB")
    for name, width, q in ((f"{i:02d}.webp", 1920, 78), (f"{i:02d}_thumb.webp", 640, 72)):
        path = os.path.join(OUT, name)
        fit(im, width).save(path, "WEBP", quality=q, method=6)
        total += os.path.getsize(path)
    if i == CARD:
        card = fit(im, 960)
        card.save(os.path.join(OUT, "card.jpg"), "JPEG", quality=84, optimize=True, progressive=True)
        card.save(os.path.join(OUT, "card.webp"), "WEBP", quality=76, method=6)
print(len(src), "shots,", total // 1024, "KB")
