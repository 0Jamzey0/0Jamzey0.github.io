"""Copies and resizes store media into the site. Run once when gallery picks change:
python tools/prepare_media.py <path to logo png>
"""
import math, os, sys
from PIL import Image

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA = "D:/StoreAssetProjects_Media/Publishing"

GALLERY = {
    "frostfall": ("Frostfall/Fab/Gallery", ".jpg", ["01_hero", "02_footprints", "03_overlay_before_after", "04_trench",
                                                    "05_shelter", "06_calm_to_blizzard", "10_wind_driven_snow", "14_presets"]),
    "downpour": ("Downpour/Fab/Gallery", ".jpg", ["01_Hero", "02_Before_After", "04_Puddles", "07_Running_Drops",
                                                  "09_Glass", "11_Shelter", "14_Lightning", "19_Presets"]),
    "carve": ("POM/Fab/Gallery", ".jpg", ["01_Hero", "02_Before_After", "03_Curved_Outlines", "05_Self_Shadows",
                                          "12_Decals", "14_Triplanar", "18_Town", "24_Materials"]),
    "editor-customizer": ("Cockpit/StoreMedia", ".png", ["01_make_it_yours", "02_one_window", "03_themes", "04_hierarchy",
                                                         "05_project", "06_quick_actions", "07_editor_health", "08_guided_tour"]),
}
CARD = {"editor-customizer": "Cockpit/StoreMedia/KeyImages/YouTube_Thumbnail_1280x720.png",
        "frostfall": "Frostfall/Fab/Thumbnail_1920x1080.jpg"}
HERO = {"frostfall": "Frostfall/Fab/Thumbnail_1920x1080.jpg"}

def save(im, path, width, q=82):
    im = im.convert("RGB")
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    im.save(path, "JPEG", quality=q, optimize=True, progressive=True)

for slug, (folder, ext, picks) in GALLERY.items():
    for name in picks:
        src = Image.open(f"{MEDIA}/{folder}/{name}{ext}")
        out = f"{SITE}/img/{slug}/{name.lower()}"
        save(src, out + ".jpg", 1600, 86 if ext == ".png" else 82)
        save(src, out + "_thumb.jpg", 640, 80 if ext == ".png" else 78)
    card = CARD.get(slug, f"{folder}/{picks[0]}{ext}")
    save(Image.open(f"{MEDIA}/{card}"), f"{SITE}/img/{slug}/card.jpg", 960, 86 if slug in CARD else 82)
    if slug in HERO:
        save(Image.open(f"{MEDIA}/{HERO[slug]}"), f"{SITE}/img/{slug}/thumbnail.jpg", 1600, 86)

social = Image.open(f"{MEDIA}/Fab_Profile/JamzeySt_Fab_Cover_1920x540.png").convert("RGB")
canvas = Image.new("RGB", (1200, 630), social.getpixel((4, 4)))
s = social.resize((1200, round(540 * 1200 / 1920)), Image.LANCZOS)
canvas.paste(s, (0, (630 - s.height) // 2))
canvas.save(f"{SITE}/img/social.jpg", "JPEG", quality=86)

# J mark from the logo: crop, key out the cream background
logo = Image.open(sys.argv[1]).convert("RGBA")
bg = logo.getpixel((2, 2))[:3]
mark = logo.crop((30, 75, 111, 174))
px = mark.load()
for y in range(mark.height):
    for x in range(mark.width):
        r, g, b, a = px[x, y]
        d = math.dist((r, g, b), bg)
        px[x, y] = (r, g, b, 0 if d < 18 else 255 if d > 60 else int((d - 18) / 42 * 255))
mark.save(f"{SITE}/img/mark.png")
icon = Image.new("RGBA", (128, 128), (0, 0, 0, 0))
m = mark.resize((round(mark.width * 116 / mark.height), 116), Image.LANCZOS)
icon.paste(m, ((128 - m.width) // 2, 6), m)
icon.save(f"{SITE}/favicon.png")
logo.convert("RGB").save(f"{SITE}/img/logo.png")
print("media ok")
