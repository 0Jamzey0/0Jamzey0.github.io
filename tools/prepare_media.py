"""Copies and resizes store media into the site. Run when gallery picks change:
python tools/prepare_media.py [slug ...] [--force] [--logo <path to logo png>]
With slugs, only those assets are processed. Existing images are skipped unless --force.
The social image, J mark and favicon are only rebuilt when --logo is given.
A pick containing "/" is a path under MEDIA with its extension (to mix folders, e.g. 1.1 store images).
"""
import math, os, sys
from PIL import Image

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA = "D:/StoreAssetProjects_Media/Publishing"

GALLERY = {
    "frostfall": ("Frostfall/Fab/Gallery", ".jpg", ["01_hero", "02_footprints", "03_overlay_before_after", "04_trench",
                                                    "05_shelter", "06_calm_to_blizzard", "10_wind_driven_snow", "14_presets"]),
    "downpour": ("Downpour/Fab/Gallery", ".jpg", ["01_Hero", "Downpour/v11_media/StoreMedia/V11_02_Lit_Rain.png",
                                                  "Downpour/v11_media/StoreMedia/V11_05_Slope_Flow.png",
                                                  "02_Before_After", "04_Puddles", "07_Running_Drops", "11_Shelter",
                                                  "Downpour/v11_media/StoreMedia/V11_07_HDRP_URP.png"]),
    "scorch": ("Scorch/Fab/Gallery", ".jpg", ["Scorch/StoreMedia/15_Enhanced_Hero.png",
                                              "Scorch/StoreMedia/16_Enhanced_Three_Modes.png",
                                              "02_Before_After", "03_Burn_Front", "04_Spread", "06_Water",
                                              "07_Explosion", "09_Night"]),
    "carve": ("POM/Fab/Gallery", ".jpg", ["01_Hero", "02_Before_After", "03_Curved_Outlines", "05_Self_Shadows",
                                          "12_Decals", "14_Triplanar", "18_Town", "24_Materials"]),
    "editor-customizer": ("Cockpit/StoreMedia", ".png", ["01_make_it_yours", "02_one_window", "03_themes", "04_hierarchy",
                                                         "05_project", "06_quick_actions", "07_editor_health", "08_guided_tour"]),
}
CARD = {"editor-customizer": "Cockpit/StoreMedia/KeyImages/YouTube_Thumbnail_1280x720.png",
        "frostfall": "Frostfall/Fab/Thumbnail_1920x1080.jpg"}
HERO = {"frostfall": "Frostfall/Fab/Thumbnail_1920x1080.jpg"}

args = sys.argv[1:]
FORCE = "--force" in args
LOGO = args[args.index("--logo") + 1] if "--logo" in args else None
ONLY = [a for i, a in enumerate(args) if not a.startswith("--") and (i == 0 or args[i - 1] != "--logo")]

def save(im, path, width, q=82):
    if os.path.exists(path) and not FORCE:
        return
    im = im.convert("RGB")
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    im.save(path, "JPEG", quality=q, optimize=True, progressive=True)

def source(folder, ext, pick):
    """(media-relative path, site name) for a gallery pick."""
    if "/" in pick:
        return pick, os.path.splitext(os.path.basename(pick))[0].lower()
    return f"{folder}/{pick}{ext}", pick.lower()

for slug, (folder, ext, picks) in GALLERY.items():
    if ONLY and slug not in ONLY:
        continue
    for pick in picks:
        rel, name = source(folder, ext, pick)
        src = Image.open(f"{MEDIA}/{rel}")
        png = rel.endswith(".png")
        out = f"{SITE}/img/{slug}/{name}"
        save(src, out + ".jpg", 1600, 86 if png else 82)
        save(src, out + "_thumb.jpg", 640, 80 if png else 78)
    card = CARD.get(slug, source(folder, ext, picks[0])[0])
    save(Image.open(f"{MEDIA}/{card}"), f"{SITE}/img/{slug}/card.jpg", 960, 86 if slug in CARD or card.endswith(".png") else 82)
    if slug in HERO:
        save(Image.open(f"{MEDIA}/{HERO[slug]}"), f"{SITE}/img/{slug}/thumbnail.jpg", 1600, 86)

if not LOGO:
    print("media ok (logo, social image and favicon unchanged)")
    sys.exit(0)

social =Image.open(f"{MEDIA}/Fab_Profile/JamzeySt_Fab_Cover_1920x540.png").convert("RGB")
canvas = Image.new("RGB", (1200, 630), social.getpixel((4, 4)))
s = social.resize((1200, round(540 * 1200 / 1920)), Image.LANCZOS)
canvas.paste(s, (0, (630 - s.height) // 2))
canvas.save(f"{SITE}/img/social.jpg", "JPEG", quality=86)

# J mark from the logo: crop, key out the cream background
logo = Image.open(LOGO).convert("RGBA")
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
