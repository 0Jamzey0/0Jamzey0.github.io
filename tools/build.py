"""Generates index.html and one page per asset. Edit the data below, then: python tools/build.py"""
import hashlib, os
from html import escape

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VER = hashlib.sha1(b"".join(open(os.path.join(SITE, f), "rb").read()
                            for f in ("css/style.css", "css/gate.css", "css/zenos.css", "js/site.js", "js/grid.js",
                                      "js/gate.js", "js/zenos.js"))).hexdigest()[:8]
URL = "https://0jamzey0.github.io/"
STORE = "https://assetstore.unity.com/publishers/100637"
YOUTUBE = "https://www.youtube.com/@Jamzey-Dev"
PATREON = "https://www.patreon.com/cw/JamzeyDev"
EMAIL = "jamzeyst@gmail.com"
FAB = "https://www.fab.com/sellers/Jamzey"
# Fill these in when they exist. Empty ones are left out of the site.
ITCH = ""          # e.g. "https://jamzey.itch.io"
DISCORD = ""       # permanent invite, e.g. "https://discord.gg/xxxx"
NEWSLETTER = ""    # signup page, e.g. "https://buttondown.com/jamzey"
GOATCOUNTER = ""   # GoatCounter site code, e.g. "jamzey" for jamzey.goatcounter.com

def ext(href, text, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f'<a{c} href="{href}" target="_blank" rel="noopener">{text}</a>'

FIND_ME = [(STORE, "Unity Asset Store"), (FAB, "Fab"), (ITCH, "itch.io"), (YOUTUBE, "YouTube"),
           (PATREON, "Patreon"), (DISCORD, "Discord"), (NEWSLETTER, "Newsletter")]

ASSETS = [
    dict(
        slug="frostfall", name="Frostfall", sub="Deformable Snow for HDRP",
        store="https://assetstore.unity.com/packages/package/412814", version="1.1.0", hero="thumbnail",
        pipelines=["HDRP"],
        tag="Snow that piles up, takes footprints and covers every object.",
        lead="Open-world snow for the High Definition Render Pipeline. Characters leave boot prints, vehicles carve "
             "trenches with pushed-up berms, and every rock, roof and crate collects snow automatically, with no "
             "material changes, while the ground under roofs and trees stays bare.",
        videos=[("mgwcO4EGvC0", "Frostfall trailer", "Footprints, snow on any object & weather"),
                ("962PG-I17fs", "Frostfall 1.1 update", "Blizzards, lens frost & snow audio")],
        features=[
            ("Deformable snow ground", ["Tessellated, subsurface-scattered snow with real displacement and shadows",
                                         "GPU deformation simulated by compute shaders, no gaps at speed",
                                         "Berms around every track, compacted floors, trample-to-slush reveal"]),
            ("Snow on any shader", ["One HDRP Custom Pass adds lit snow to every opaque object",
                                    "No material changes: HDRP/Lit, Shader Graph and third-party shaders",
                                    "Sky occlusion keeps roofs, bridges and tree canopies sheltered"]),
            ("Weather & presets", ["Snowfall accumulation, thaw, wetness and track refill",
                                   "Blizzards, wind-driven snow and lens frost (1.1)",
                                   "5 presets, swappable at runtime"]),
            ("Characters & vehicles", ["One-click footprints for any humanoid, fitted from the rig",
                                       "WheelCollider ruts, hooves, debris and ragdoll contact",
                                       "Contact events plus particle and audio hooks"]),
            ("Workflow", ["Setup Wizard that checks and fixes your project in one click",
                          "Snow Cover material converts HDRP/Lit in place",
                          "Live track preview and red/green debug gizmos"]),
            ("Ships with", ["Playable showcase demo with a weather panel, plus a minimal demo",
                            "Clean C# API, assembly definitions and PDF documentation",
                            "All textures, meshes and shaders are original"]),
        ],
        gallery=[("01_hero", "Frostfall hero scene"), ("02_footprints", "Footprints in fresh powder"),
                 ("03_overlay_before_after", "Snow overlay before and after"), ("04_trench", "Vehicle trench with berms"),
                 ("05_shelter", "Sheltered ground under roofs"), ("06_calm_to_blizzard", "Calm to blizzard"),
                 ("10_wind_driven_snow", "Wind-driven snow"), ("14_presets", "Snow presets")],
        specs=[("Unity", "6.0 LTS or newer"), ("Render pipeline", "HDRP 17.0+"),
               ("Graphics APIs", "DX11, DX12, Vulkan, Metal"), ("Version", "1.1.0"),
               ("Demo scenes", "Showcase + minimal"), ("Content", "100% original")],
    ),
    dict(
        slug="downpour", name="Downpour", sub="Rain & Wet Surfaces for HDRP & URP",
        store="https://assetstore.unity.com/packages/package/415192", version="1.1",
        pipelines=["HDRP", "URP"],
        tag="Rain-soaked scenes without touching a single material.",
        lead="Streets darken and gloss, puddles fill the low spots, water runs down walls and slopes, drops run down "
             "glass and cars, rain glints in your streetlamps, and everything under a roof stays dry. It works on "
             "every object whatever shader it uses, in HDRP and URP.",
        videos=[("Shq2jn_EiPQ", "Downpour trailer", "Rain & wet surfaces for HDRP"),
                ("Aodo_yMEnO4", "Downpour 1.1 update", "URP, rain lit by local lights & water on slopes")],
        new=("New in 1.1", ["URP support in Forward, Forward+ and Deferred, set up by the Setup Wizard",
                            "Rain lit by local lights: drops glint in streetlamps, neon and headlights",
                            "Water flowing on slopes, gathering into channels along gutters and curbs",
                            "Wall streams that come and go and start again under every ledge",
                            "A new editor: live dry/wet preview, forecast strip, scene checks and GPU cost per system"]),
        features=[
            ("Wet surfaces, any shader", ["Porous materials darken, everything turns glossy",
                                          "Water film on level ground and runnels down walls",
                                          "Forward-only materials (hair, fabric, StackLit) get a sheen"]),
            ("Puddles & ripples", ["Puddles fill dips and gutters, stable from any distance",
                                   "Soaked rims and deeper, darker water in the middle",
                                   "Raindrop ripples plus rings from drips and footsteps"]),
            ("Drops on every object", ["Drops cling, slide in stick-slip bursts and leave trails",
                                       "Beads only on water-repellent surfaces like paint, metal and glass",
                                       "Glass and transparent materials included"]),
            ("Moving objects", ["Drops ride along with characters, vehicles and props",
                                "Each object soaks up in the rain and dries under cover",
                                "Footstep rings, splashes and damp prints"]),
            ("Shelter & runoff", ["Roofs, awnings, glass canopies and car interiors stay dry, no colliders needed",
                                  "Drops fall from free edges and splash where they leave",
                                  "Eaves drip from a few points, like real gutters"]),
            ("Rain & weather", ["Refracting rain streaks with wind and gusts, hidden under roofs",
                                "Lightning, lens drops, rain haze and mist",
                                "5 presets blended at runtime, scripting API and events"]),
        ],
        gallery=[("01_hero", "Downpour hero street"), ("v11_02_lit_rain", "Rain lit by streetlamps"),
                 ("v11_05_slope_flow", "Water flowing down a slope"), ("02_before_after", "Dry and wet, before and after"),
                 ("04_puddles", "Puddles with ripples"), ("07_running_drops", "Running drops"),
                 ("11_shelter", "Dry under shelter"), ("v11_07_hdrp_urp", "HDRP and URP side by side")],
        specs=[("Unity", "6.0 LTS or newer"), ("Render pipelines", "HDRP 17.0+ & URP 17.0+"),
               ("Approach", "No material changes"), ("Version", "1.1"),
               ("Demo scenes", "Showcase street + minimal"), ("Content", "100% original")],
    ),
    dict(
        slug="carve", name="Carve", sub="Silhouette Parallax Occlusion Mapping for HDRP & URP",
        store="https://assetstore.unity.com/packages/package/418204", version="1.1",
        pipelines=["HDRP", "URP"],
        tag="Real depth on flat surfaces, with carved outlines and true intersections.",
        lead="Parallax occlusion mapping built to hold up where classic POM falls apart: mesh edges are carved into "
             "the shape of the relief, props meet it at its true depth, and light, shadows and reflections follow "
             "every crack. One package for HDRP and URP.",
        videos=[("LmxFYLq_1uU", "Carve trailer", "Silhouette POM for HDRP & URP"),
                ("seBE1ZuqZ9U", "Carve 1.1 update", "Terrain, interiors, Height Fixer & faster anti-tiling")],
        new=("New in 1.1", ["Carve Terrain: real relief, self-shadows and height-blended borders on Unity Terrain",
                            "Carve Interior: a furnished room behind every window, with real depth and no extra geometry",
                            "Height Fixer finds inverted, squashed, seamed or noisy height maps and saves a fixed copy",
                            "Up to twice as fast with an identical image; Fast anti-tiling saves up to 58% GPU time",
                            "1.0 materials upgrade themselves when the update imports"]),
        features=[
            ("Real depth, real outlines", ["Carved silhouettes on box and modular edges",
                                           "Bumpy outlines on curved meshes like rocks and columns",
                                           "Pixel depth offset: props, decals, SSAO and fog meet the true depth"]),
            ("Light that reads the relief", ["Soft self-shadows that widen with distance",
                                             "Relief occlusion, no glowing cracks in wet or shiny relief",
                                             "Cast shadows carry the carved shape"]),
            ("Fast by design", ["Auto LOD and pyramid tracing",
                                "Quality Manager with Low to Ultra presets and a live readout",
                                "Adaptive quality holds a target frame rate, resolution untouched"]),
            ("Works on anything", ["Triplanar mapping for meshes without good UVs",
                                   "One-click silhouette bake for modular kits",
                                   "Carve POM node for your own Shader Graphs"]),
            ("Layers & decals", ["Up to 4 height-blended layers painted in the Scene view",
                                 "Carve Decals: cracks, bullet holes and grates cut into any surface",
                                 "Turn the relief into a collider or a detailed mesh"]),
            ("No setup headaches", ["13 ready-to-use materials for both pipelines",
                                    "Height map generator and one-click converter from Lit",
                                    "Carve Hub, three demo scenes per pipeline and a 28-page manual"]),
        ],
        gallery=[("01_hero", "Carve walled town"), ("02_before_after", "Classic POM versus Carve"),
                 ("03_curved_outlines", "Curved outlines"), ("05_self_shadows", "Relief self-shadows"),
                 ("12_decals", "Carve Decals"), ("14_triplanar", "Triplanar mapping"),
                 ("18_town", "Town built with Carve"), ("24_materials", "Included materials")],
        specs=[("Unity", "6.0 LTS or newer"), ("Render pipelines", "HDRP & URP"),
               ("Materials", "13 included"), ("Version", "1.1"),
               ("Demo scenes", "3 per pipeline"), ("Content", "100% original")],
    ),
    dict(
        slug="scorch", name="Scorch", sub="Dynamic Fire & Burn System for HDRP",
        store="https://assetstore.unity.com/packages/package/421656", version="1.1",
        pipelines=["HDRP"],
        tag="Fire that spreads, chars and burns through any object, without changing its materials.",
        lead="Mark objects as flammable and they catch, burn, char, smoulder and go out. A glowing front crawls "
             "across each surface, neighbours heat up and catch in turn, and water puts it all out again. The char "
             "is drawn as a decal, so it works on your existing HDRP materials without changing a single one.",
        videos=[("wIvYNtdIUYg", "Scorch trailer", "Dynamic fire & burn system for HDRP"),
                ("udAjyNgGtLE", "Scorch 1.1 update", "Particles Enhanced: sharp, realistic flames")],
        features=[
            ("Burns what you have", ["Char, soot and glowing embers on your existing HDRP materials",
                                     "A glowing burn front that climbs faster than it spreads down",
                                     "Burns move with the object, and burnt stays burnt"]),
            ("Fire that behaves", ["Spreads object to object, faster downwind and upward",
                                   "7 material presets, from paper and hay to hardwood beams",
                                   "Dies down into smouldering embers before going out"]),
            ("Three flame modes", ["Particles: soft, layered and cheap enough for a burning street",
                                   "Particles Enhanced (1.1): sharp, torn flames baked from a 3D combustion simulation",
                                   "Volumetric: a live 3D simulation for hero fires; switch any time"]),
            ("Water & explosions", ["Hoses, buckets and rain put fires out in a burst of steam",
                                    "Soaked walls make firebreaks that dry out again",
                                    "Explosive objects with chain reactions, or explosions in one call"]),
            ("Smoke, light & sound", ["Smoke by fuel, sparks, embers, ash and heat haze",
                                      "Firelight with soft shadows; soot and blast marks on any surface",
                                      "Original fire, crackle, steam and explosion sounds"]),
            ("Workflow", ["Fire Manager with a live monitor and one-click setup check",
                          "Quality tiers Low to Ultra with a live cost readout (1.1)",
                          "C# API with events, heat queries and save/restore"]),
        ],
        gallery=[("15_enhanced_hero", "Particles Enhanced flames"), ("16_enhanced_three_modes", "Three flame modes"),
                 ("02_before_after", "Before and after the fire"), ("03_burn_front", "Glowing burn front"),
                 ("04_spread", "Fire spreading between objects"), ("06_water", "Water putting the fire out"),
                 ("07_explosion", "Explosive barrels"), ("09_night", "Firelight at night")],
        specs=[("Unity", "6.0 LTS or newer"), ("Render pipeline", "HDRP 17.0+"),
               ("Flame modes", "Particles, Enhanced, Volumetric"), ("Version", "1.1"),
               ("Demo scenes", "3, incl. a 100-object large-scale demo"), ("Content", "100% original")],
    ),
    dict(
        slug="editor-customizer", name="Editor Customizer", sub="Themes, Hierarchy, Toolbar & Editor Health",
        store=None, status="Coming soon", version="1.0.0",
        pipelines=["Built-in", "URP", "HDRP"], chipset=("Built-in", "URP", "HDRP"),
        tag="Make the Unity editor yours: your colours, a Hierarchy you read at a glance, your tools one click away.",
        lead="Five modules in one window, each with its own switch: themes for every Unity panel, a Hierarchy and "
             "Project you can read at a glance, your tools one click away, and a health check that tells you in "
             "plain words why Unity is slow. Nothing changes until you say so.",
        videos=[("video/editor-customizer-trailer.mp4", "Editor Customizer trailer",
                 "Themes, Hierarchy, toolbar & Editor Health")],
        features=[
            ("Make it yours", ["Recolour the whole editor from four colours",
                               "Presets, your own themes, and theme files to share with your team",
                               "A Play Mode colour wash so you never edit while playing by accident",
                               "Any font, bold or italic, and text size from 80 to 130%"]),
            ("Find things at a glance", ["Header rows that never reach your builds",
                                         "Row colours and icons, plus rules by component, tag, layer or name",
                                         "Coloured folders with badges; common folders colour themselves",
                                         "270+ hand-picked icons plus Unity's 1,300+ built-in icons"]),
            ("Your tools in reach", ["One-click actions for any menu item, with your own keys",
                                     "Scene switcher, Play From First Scene and Fast Play",
                                     "Play Mode time scale, frame-rate cap and one-click screenshots"]),
            ("Editor Health", ["One plain sentence a day on how long Unity made you wait, and why",
                               "Every compile, domain reload and Play Mode change timed, with a 7-day chart",
                               "Slow [InitializeOnLoad] callbacks named and grouped by package",
                               "Memory warnings and a console grouped by package"]),
            ("Safe by default", ["Every module starts switched off",
                                 "One click puts back Unity's own look, exactly",
                                 "Nothing is written into your scenes, prefabs or the Unity install",
                                 "Styles live in a ProjectSettings file your team shares"]),
            ("Built to extend", ["One window with search, a switch and a card for each module",
                                 "A hands-on guided tour in the demo scene",
                                 "Write your own modules by deriving one class",
                                 "Theme switch in about 50 ms; under 0.02% of editor time when on"]),
        ],
        gallery=[("01_make_it_yours", "Editor Customizer versus Unity's default look"),
                 ("02_one_window", "One window for every module"), ("03_themes", "Editor themes"),
                 ("04_hierarchy", "Hierarchy styling"), ("05_project", "Project folder colours"),
                 ("06_quick_actions", "Toolbar and quick actions"), ("07_editor_health", "Editor Health"),
                 ("08_guided_tour", "Guided tour in the demo scene")],
        specs=[("Unity", "6.0 LTS or newer"), ("Render pipelines", "Any: Built-in, URP, HDRP"),
               ("Runs in", "Editor only, nothing added to builds"), ("Version", "1.0.0"),
               ("Demo", "Guided tour scene"), ("Manual", "22-page PDF")],
    ),
]

UPCOMING = [
    dict(slug="dustfall", name="Dustfall", sub="Sand, Dust & Sandstorms for HDRP", pipelines=["HDRP"],
         status="In development",
         tag="Sand that takes footprints and tire tracks, dust on every surface, and towering sandstorms."),
    dict(slug="amberfall", name="Amberfall", sub="Autumn Leaves & Seasonal Foliage for HDRP & URP",
         pipelines=["HDRP", "URP"], status="In development",
         tag="Autumn leaves that fall, gather and drift through your scenes as the season turns."),
]

# ---------------------------------------------------------------- P_Zenos
# Its own site inside the site (pzenos.html). Shots are img/pzenos/NN.webp, numbered in filename order by
# tools/prepare_zenos.py from F:/P_ZeonVer1/Screenshots. Edit any text below, then rebuild.
PZ_SLOGAN = "The One that Started it All"
PZ_SHOTS = {
    0: "Close-up", 1: "Close-up", 2: "Face to face", 3: "Ready to go", 4: "Over the shoulder", 5: "Into the sun",
    6: "Going prone", 7: "Rifle up", 8: "Swimming", 9: "Cutting through the surface", 10: "Under the surface",
    11: "Diving deep", 12: "Underwater", 13: "At the water's edge", 14: "Ladder climb",
    15: "Climbing out of the water", 16: "Swimming the pool", 17: "Balance beam", 18: "Holding a breath",
    19: "Boat on open water", 20: "Full throttle", 21: "At the wheel", 22: "The wake from above", 23: "On the move",
    24: "Explosion", 25: "The horse", 26: "Up against the wall", 27: "Into the light", 28: "Laser sight",
}
PZ_HERO = [5, 14, 21, 11, 24, 25, 7]          # hero slideshow, in order
PZ_STORY_SHOT = 2
PZ_BIG = {5, 11, 21, 24, 14}                  # larger tiles in the photo grid
PZ_WINDOWS = [                                # (id, tab, title, text, shots)
    ("water", "Water", "Into the water", "Swim the surface, then dive below it and hold your breath.", [9, 8, 11, 12, 18, 16]),
    ("climb", "Climb", "Up and over", "Ladders, walls, ledges and narrow beams.", [14, 15, 26, 17, 13]),
    ("boats", "Boats", "Open water", "Take the wheel and cut across the waves.", [21, 19, 20, 22]),
    ("ride", "Ride", "Saddle up", "A horse for the long road.", [25]),
    ("action", "Action", "Under fire", "Aim, fire and get clear of the blast.", [24, 7, 28, 6]),
    ("hero", "Hero", "The hero", "Up close with the one who started it all.", [2, 0, 3, 4, 5, 27, 23]),
]
PZ_VIDEOS = []                                # add (youtube_id, title, note) when the first devlog is up
PZ_STATS = [("Unity 6", "Engine"), ("HDRP", "Pipeline"), ("Ray tracing", "Lighting"), ("In development", "Status")]

def pz_img(n, thumb=False):
    return f"img/pzenos/{n:02d}{'_thumb' if thumb else ''}.webp"

def letters(word, cls="pz-word"):
    """A word split into letters for staggered animation; screen readers get the whole word."""
    return (f'<span class="{cls}"><span class="pz-sr">{escape(word)}</span>' +
            "".join(f'<span aria-hidden="true" style="--i:{i}">{escape(c)}</span>' for i, c in enumerate(word)) +
            "</span>")

_TICKS = "".join(f'<line x1="50" y1="5.5" x2="50" y2="{9.5 if i % 3 == 0 else 7.5}" transform="rotate({i * 10} 50 50)"/>'
                 for i in range(36))
EMBLEM = (
    '<svg class="pz-emblem" viewBox="0 0 100 100" aria-hidden="true" focusable="false">'
    '<circle class="pz-ring" cx="50" cy="50" r="46" transform="rotate(-90 50 50)"/>'
    '<circle class="pz-ring2" cx="50" cy="50" r="38"/>'
    f'<g class="pz-ticks">{_TICKS}</g>'
    '<g class="pz-star"><path d="M50 13 L55.5 44.5 L87 50 L55.5 55.5 L50 87 L44.5 55.5 L13 50 L44.5 44.5Z"/>'
    '<path class="pz-star2" d="M50 28 L52.5 47.5 L72 50 L52.5 52.5 L50 72 L47.5 52.5 L28 50 L47.5 47.5Z" transform="rotate(45 50 50)"/></g>'
    '<circle class="pz-hub" cx="50" cy="50" r="4.5"/></svg>'
)
_WAVE = "M0 30 Q150 0 300 30 T600 30 T900 30 T1200 30 V60 H0Z"
_BUBBLES = "".join(f'<i style="--x:{x}%;--s:{s}px;--d:{d}s;--w:{w}s"></i>' for x, s, d, w in [
    (6, 10, 3.4, 0), (14, 6, 2.8, .6), (22, 14, 4.2, .2), (31, 8, 3.1, 1.1), (39, 5, 2.6, .4), (47, 12, 3.8, .9),
    (55, 7, 2.9, .1), (63, 16, 4.6, .7), (71, 6, 2.7, 1.3), (78, 10, 3.5, .3), (86, 8, 3.0, .8), (93, 13, 4.0, .5)])

def gate(state=""):
    cls = f"pz-gate {state}".strip()
    return (f'<div class="{cls}" id="pz-gate" aria-hidden="true">'
            f'<div class="pz-water"><svg class="pz-wave back" viewBox="0 0 1200 60" preserveAspectRatio="none"><path d="{_WAVE}"/></svg>'
            f'<svg class="pz-wave" viewBox="0 0 1200 60" preserveAspectRatio="none"><path d="{_WAVE}"/></svg></div>'
            f'<div class="pz-bubbles">{_BUBBLES}</div>'
            f'<div class="pz-gate-core">{EMBLEM}{letters("P_ZENOS")}<p class="pz-slogan">{escape(PZ_SLOGAN)}</p></div></div>')

def chips(a):
    return '<div class="chips">' + "".join(
        f'<span class="chip{" on" if p in a["pipelines"] else ""}">{p}</span>'
        for p in a.get("chipset", ("HDRP", "URP"))) + "</div>"

def store_button(a, label):
    if a["store"]:
        return f'<a class="btn btn-primary" href="{a["store"]}" target="_blank" rel="noopener">{label}</a>'
    return '<span class="btn btn-soon" aria-disabled="true">Coming soon to the Asset Store</span>'

def head(title, desc, path=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{URL}{path}">
<meta property="og:image" content="{URL}img/{'social' if not path else path.replace('.html', '') + '/card'}.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#E9E7DA">
<script>try{{if(localStorage.getItem("theme")==="dark"){{document.documentElement.dataset.theme="dark";document.querySelector('meta[name="theme-color"]').content="#141312"}}}}catch(e){{}}</script>
<script>try{{if(sessionStorage.getItem("pz-nav")==="jamzey"&&!matchMedia("(prefers-reduced-motion: reduce)").matches)document.documentElement.classList.add("jz-arrive")}}catch(e){{}}</script>
<link rel="icon" href="favicon.png">
<link rel="preload" href="fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="css/style.css?v={VER}">
<link rel="stylesheet" href="css/gate.css?v={VER}">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top">
  <div class="wrap">
    <a class="brand" href="index.html"><img src="img/mark.webp" alt="" width="28" height="34" decoding="async">Jamzey St.</a>
    <button class="menu-btn" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
    <nav class="nav">
      <a href="index.html#assets">Assets</a>
      <a href="index.html#videos">Videos</a>
      <a href="index.html#about">About</a>
      <a class="nav-pz" href="pzenos.html" data-zenos>P_Zenos</a>
      {ext(PATREON, "Patreon")}{(chr(10) + "      " + ext(DISCORD, "Discord")) if DISCORD else ""}
      {ext(STORE, "Asset Store", "btn btn-primary btn-small")}
    </nav>
    <button class="theme-toggle" type="button" aria-label="Night mode" aria-pressed="false" title="Switch to night mode">
      <span class="tt-sky" aria-hidden="true"><i class="tt-cloud c1"></i><i class="tt-cloud c2"></i><i class="tt-star s1"></i><i class="tt-star s2"></i><i class="tt-star s3"></i><i class="tt-star s4"></i></span>
      <span class="tt-knob" aria-hidden="true"><svg class="tt-icon" viewBox="0 0 24 24">
        <mask id="tt-moon"><rect width="24" height="24" fill="#fff"/><circle class="tt-bite" cx="17.5" cy="7" r="6.5" fill="#000"/></mask>
        <g mask="url(#tt-moon)"><circle class="tt-core" cx="12" cy="12" r="5"/></g>
        <path class="tt-rays" d="M12 1.8v2.4M12 19.8v2.4M1.8 12h2.4M19.8 12h2.4M4.8 4.8l1.7 1.7M17.5 17.5l1.7 1.7M4.8 19.2l1.7-1.7M17.5 6.5l1.7-1.7"/>
      </svg></span>
    </button>
  </div>
</header>
"""

FOOT = f"""<footer>
  <div class="wrap">
    <div>
      <a class="brand" href="index.html"><img src="img/mark.webp" alt="" width="28" height="34" decoding="async">Jamzey St.</a>
      <p class="blurb">Weather, surface and VFX tools for Unity. Built and tested in Unity 6.</p>
    </div>
    <div>
      <h4>Assets</h4>
      <ul>{"".join(f'<li><a href="{a["slug"]}.html">{a["name"]}</a></li>' for a in ASSETS)}<li><a href="pzenos.html" data-zenos>P_Zenos</a></li></ul>
    </div>
    <div>
      <h4>Find me</h4>
      <ul>
        {"".join(f"<li>{ext(h, t)}</li>" for h, t in FIND_ME if h)}
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
      </ul>
    </div>
    <p class="fine">© 2026 Jamzey St. Unity is a trademark of Unity Technologies; this site is not affiliated with Unity.</p>
  </div>
</footer>
<script src="js/site.js?v={VER}"></script>
<script src="js/grid.js?v={VER}"></script>
<template id="pz-gate-tpl">{gate()}</template>
<script src="js/gate.js?v={VER}"></script>{f'''
<script data-goatcounter="https://{GOATCOUNTER}.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>''' if GOATCOUNTER else ""}
</body>
</html>
"""

def video(vid, title, note):
    cap = f'<figcaption>{escape(title)}<small>{escape(note)}</small></figcaption>'
    if vid.endswith(".mp4"):
        poster = "img/" + vid.split("/")[1].replace("-trailer.mp4", "") + "/card.webp"
        return (f'<figure class="video"><div class="yt-frame"><video controls preload="none" playsinline '
                f'poster="{poster}" aria-label="{escape(title)}"><source src="{vid}" type="video/mp4"></video></div>{cap}</figure>')
    return (f'<figure class="video"><button class="yt" data-id="{vid}" aria-label="Play {escape(title)}">'
            f'<span class="play"></span></button>{cap}</figure>')

def card(a):
    return f"""<a class="card" href="{a['slug']}.html">
  <div class="shot">{f'<span class="status">{a["status"]}</span>' if a.get("status") else ""}<img src="img/{a['slug']}/card.webp" alt="{a['name']}" loading="lazy" decoding="async" width="960" height="540"></div>
  <div class="body">
    {chips(a)}
    <h3>{a['name']}</h3>
    <span class="tag">{escape(a['sub'])}</span>
    <p>{escape(a['tag'])}</p>
    <span class="more">View asset →</span>
  </div>
</a>"""

def teaser(a):
    return f"""<a class="card soon {a['slug']}" href="{PATREON}" target="_blank" rel="noopener">
  <div class="shot teaser"><span class="status">{a['status']}</span><strong>{a['name']}</strong></div>
  <div class="body">
    {chips(a)}
    <span class="tag">{escape(a['sub'])}</span>
    <p>{escape(a['tag'])}</p>
    <span class="more">Follow progress on Patreon →</span>
  </div>
</a>"""

def index():
    # One video per asset on the homepage (its main trailer); updates stay on the product pages.
    vids = [a["videos"][0] for a in sorted(ASSETS, key=lambda a: bool(a["store"]))]
    live = sum(1 for a in ASSETS if a["store"])
    return head("Jamzey St. · Weather, surfaces & VFX for Unity",
                "Drop-in environment tools for Unity: deformable snow, rain and wet surfaces, spreading fire, and "
                "silhouette parallax occlusion mapping for HDRP and URP.") + f"""
<main id="main">
<section class="hero">
  <img class="blocks blocks-left" src="img/blocks-left.svg" alt="" width="345" height="274" decoding="async">
  <img class="blocks blocks-right" src="img/blocks-right.svg" alt="" width="566" height="562" decoding="async">
  <div class="wrap">
    <span class="eyebrow">Jamzey St.</span>
    <h1>Weather, surfaces <em>&amp;</em> VFX</h1>
    <p class="lead">Drop-in environment tools for Unity. Snow that takes footprints, rain that soaks every surface,
      fire that spreads and chars, and relief with real depth, all working on any shader with no material changes.</p>
    <div class="cta">
      <a class="btn btn-primary" href="#assets">Browse assets</a>
      <a class="btn btn-ghost" href="#videos">Watch the trailers</a>
    </div>
  </div>
</section>
<div class="facts">
  <span>{live} assets on the Unity Asset Store</span>
  <span>Built for Unity 6</span>
  <span>HDRP &amp; URP</span>
  <span>Demo scenes + full documentation</span>
</div>

<section id="assets">
  <div class="wrap">
    <div class="sec-head">
      <div><div class="kicker">Asset Store</div><h2>The <em>assets</em></h2></div>
      <p>Each package drops into an existing scene, ships with playable demos, and is documented for people who'd
        rather build their game than read a manual.</p>
    </div>
    <div class="cards{' two' if len(ASSETS) % 3 else ''}">
{"".join(card(a) for a in ASSETS)}
    </div>
  </div>
</section>

<section id="pzenos" class="pz-portal">
  <div class="wrap">
    <a class="pz-portal-link" href="pzenos.html" data-zenos>
      <span class="pz-portal-bg"><img src="{pz_img(19)}" alt="" loading="lazy" decoding="async" width="1920" height="1080"></span>
      <span class="pz-portal-in">
        {EMBLEM}
        <span class="pz-portal-kicker">Where it all began</span>
        {letters("P_ZENOS")}
        <span class="pz-slogan">{escape(PZ_SLOGAN)}</span>
        <span class="pz-portal-cta">Enter P_Zenos →</span>
      </span>
    </a>
  </div>
</section>

<section id="upcoming">
  <div class="wrap">
    <div class="sec-head">
      <div><div class="kicker">In the workshop</div><h2>Coming <em>next</em></h2></div>
      <p>Sand and autumn leaves are on the bench. Patreon members see them first.</p>
    </div>
    <div class="cards{' two' if len(UPCOMING) % 3 else ''}">
{"".join(teaser(a) for a in UPCOMING)}
    </div>
  </div>
</section>

<section id="videos" class="dark">
  <div class="wrap">
    <div class="sec-head">
      <div><div class="kicker">Videos</div><h2>See them <em>in motion</em></h2></div>
      <p>Trailers and update videos, captured in real time in Unity.</p>
    </div>
    <div class="videos{' lead-wide' if len(vids) % 2 else ''}">
{"".join(video(*v) for v in vids)}
    </div>
    <div class="channel"><a class="btn btn-ghost" href="{YOUTUBE}" target="_blank" rel="noopener">Visit the YouTube channel</a></div>
  </div>
</section>

<section id="about">
  <div class="wrap about">
    <div class="text">
      <div class="kicker">About</div>
      <h2>Making worlds feel <em>alive</em></h2>
      <p>Jamzey St. is an independent studio making environment tools for Unity: snow that piles up and takes
        footprints, rain that soaks surfaces, fire that spreads and chars, and surfaces with real depth.</p>
      <p>Every package is built and tested in Unity 6, uses its own original textures, meshes and shaders, and is
        designed to work with the scenes and shaders you already have.</p>
    </div>
    <div class="promises">
      <div class="promise"><i>01</i><div><b>Any shader, no material changes</b><span>Effects layer onto your existing scene through render passes.</span></div></div>
      <div class="promise"><i>02</i><div><b>Playable demo scenes</b><span>Every feature has a spot in a demo you can walk around in.</span></div></div>
      <div class="promise"><i>03</i><div><b>One-click setup</b><span>Setup Wizards check your project and fix what's missing.</span></div></div>
      <div class="promise"><i>04</i><div><b>Documented & supported</b><span>PDF manuals, a clean C# API, and every message gets read.</span></div></div>
    </div>
  </div>
</section>

<div class="band">
  <div class="wrap">
    <div>
      <h2>Follow what's next</h2>
      <p>P_Zenos devlogs, work-in-progress builds, behind-the-scenes breakdowns and early looks at upcoming assets.</p>
    </div>
    <div class="cta" style="display:flex;gap:12px;flex-wrap:wrap">
      {ext(PATREON, "Join on Patreon", "btn")}{(chr(10) + "      " + ext(NEWSLETTER, "Get launch emails", "btn btn-ghost")) if NEWSLETTER else ""}{(chr(10) + "      " + ext(DISCORD, "Join the Discord", "btn btn-ghost")) if DISCORD else ""}
      <a class="btn btn-ghost" href="mailto:{EMAIL}">Get in touch</a>
    </div>
  </div>
</div>
</main>
""" + FOOT

def product(a):
    others = [o for o in ASSETS if o is not a]
    return head(f"{a['name']} · {a['sub']} · Jamzey St.", a["tag"] + " " + a["lead"][:120],
                f"{a['slug']}.html") + f"""
<main id="main">
<section class="p-hero">
  <div class="wrap">
    <div>
      <a class="crumb" href="index.html#assets">← All assets</a>
      {chips(a)}
      <h1 style="margin-top:16px">{a['name']}</h1>
      <p class="sub">{escape(a['sub'])}</p>
      <p class="lead">{escape(a['lead'])}</p>
      <div class="cta">
        {store_button(a, "Get it on the Asset Store")}
        <a class="btn btn-ghost" href="#video">Watch the trailer</a>
      </div>
    </div>
    <div class="shot"><img src="img/{a['slug']}/{a.get('hero', a['gallery'][0][0])}.webp" alt="{escape(a['name'] + ' – ' + a['sub'])}" width="1600" height="900" fetchpriority="high" decoding="async"></div>
  </div>
</section>

<section id="video" class="dark">
  <div class="wrap">
    <div class="sec-head"><div><div class="kicker">Video</div><h2>{a['name']} <em>in motion</em></h2></div></div>
    <div class="videos{' one' if len(a['videos']) == 1 else ''}">
{"".join(video(*v) for v in a['videos'])}
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head"><div><div class="kicker">Features</div><h2>What's <em>inside</em></h2></div></div>
    <div class="features">
{"".join(f'<div class="feature{" wide" if i == 0 and "new" in a else ""}"><h3>{escape(t)}</h3><ul>{"".join(f"<li>{escape(x)}</li>" for x in items)}</ul></div>' for i, (t, items) in enumerate(([a["new"]] if "new" in a else []) + a['features']))}
    </div>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="sec-head"><div><div class="kicker">Gallery</div><h2>Screenshots</h2></div><p>Click any shot to view it full size.</p></div>
    <div class="gallery">
{"".join(f'<button data-full="img/{a["slug"]}/{f}.webp"><img src="img/{a["slug"]}/{f}_thumb.webp" alt="{escape(alt)}" loading="lazy" decoding="async" width="640" height="360"></button>' for f, alt in a['gallery'])}
    </div>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="sec-head"><div><div class="kicker">Technical details</div><h2>Requirements</h2></div></div>
    <dl class="specs">
{"".join(f'<div><dt>{escape(k)}</dt><dd>{escape(v)}</dd></div>' for k, v in a['specs'])}
    </dl>
    <div style="margin-top:36px">{store_button(a, f"View {a['name']} on the Asset Store")}</div>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="sec-head"><div><div class="kicker">More from Jamzey St.</div><h2>Other assets</h2></div></div>
    <div class="cards{' two' if len(others) % 3 else ''}">
{"".join(card(o) for o in others)}
    </div>
  </div>
</section>
</main>
<dialog class="lightbox">
  <img alt="">
  <p></p>
  <button class="lb-btn lb-prev" aria-label="Previous">‹</button>
  <button class="lb-btn lb-next" aria-label="Next">›</button>
  <button class="lb-btn lb-close" aria-label="Close">✕</button>
</dialog>
""" + FOOT

def zenos():
    title = f"P_Zenos · {PZ_SLOGAN} · Jamzey St."
    desc = ("P_Zenos is a cinematic third-person action-adventure in development in Unity 6 with HDRP and ray "
            "tracing, and the project Jamzey St. began with. Devlogs and updates on Patreon.")
    pad = lambda n: f"{n:02d}"
    first, rest = ' class="on" fetchpriority="high"', ' loading="lazy"'
    slides = "".join(
        f'<img src="{pz_img(n)}" alt="{escape(PZ_SHOTS[n])}" width="1920" height="1080" decoding="async"{first if i == 0 else rest}>'
        for i, n in enumerate(PZ_HERO))
    dots = "".join(f'<button type="button" aria-label="Show shot {i + 1}"></button>' for i in range(len(PZ_HERO)))
    tabs = "".join(
        f'<button type="button" role="tab" id="tab-{w}" aria-controls="win-{w}" aria-selected="{"true" if i == 0 else "false"}"'
        f' tabindex="{0 if i == 0 else -1}">{escape(t)}</button>'
        for i, (w, t, *_rest) in enumerate(PZ_WINDOWS))
    windows = "".join(f"""
<div class="pz-window" id="win-{w}" role="tabpanel" aria-labelledby="tab-{w}"{"" if i == 0 else " hidden"}>
  <div class="pz-bar"><i></i><i></i><i></i><b>P_Zenos</b> / {escape(t)}<span class="rec">Live in Unity</span></div>
  <div class="pz-win-body">
    <figure class="pz-view"><img src="{pz_img(shots[0])}" alt="{escape(PZ_SHOTS[shots[0]])}" width="1920" height="1080" loading="lazy" decoding="async"></figure>
    <div class="pz-side">
      <span class="pz-count">01 / {pad(len(shots))}</span>
      <h3>{escape(h)}</h3>
      <p>{escape(text)}</p>
      <div class="pz-thumbs">{"".join(f'<button type="button" data-full="{pz_img(n)}" aria-pressed="{"true" if j == 0 else "false"}" aria-label="{escape(PZ_SHOTS[n])}"><img src="{pz_img(n, True)}" alt="{escape(PZ_SHOTS[n])}" width="640" height="360" loading="lazy" decoding="async"></button>' for j, n in enumerate(shots))}</div>
    </div>
  </div>
</div>""" for i, (w, t, h, text, shots) in enumerate(PZ_WINDOWS))
    if PZ_VIDEOS:
        videos = f'<div class="pz-videos">{"".join(video(*v) for v in PZ_VIDEOS)}</div>'
    else:
        on = ' class="on"'
        soon = "".join(f'<img src="{pz_img(n)}" alt="" width="1920" height="1080" loading="lazy" decoding="async"{on if i == 0 else ""}>'
                       for i, n in enumerate([27, 19, 11, 24, 14]))
        videos = f"""<div class="pz-window pz-soon">
  <div class="pz-bar"><i></i><i></i><i></i><b>P_Zenos</b> / Devlog 01<span class="rec">In the edit</span></div>
  <figure class="pz-view">{soon}
    <figcaption class="pz-soon-in">
      <strong>Devlog 01 is coming</strong>
      <p>The first P_Zenos devlog is being cut right now. Subscribe on YouTube, or join on Patreon to see it first.</p>
      <span class="cta">{ext(PATREON, "Join on Patreon", "pz-btn")}{ext(YOUTUBE, "Subscribe on YouTube", "pz-ghost")}</span>
    </figcaption>
  </figure>
</div>"""
    gallery = "".join(
        f'<button type="button" class="{"big" if n in PZ_BIG else ""}" data-full="{pz_img(n)}" data-n="{pad(n)}">'
        f'<img src="{pz_img(n, n not in PZ_BIG)}" alt="{escape(PZ_SHOTS[n])}" loading="lazy" decoding="async" width="{1920 if n in PZ_BIG else 640}" height="{1080 if n in PZ_BIG else 360}"></button>'
        for n in sorted(PZ_SHOTS))
    stats = "".join(f"<div><b>{escape(v)}</b><span>{escape(k)}</span></div>" for v, k in PZ_STATS)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{URL}pzenos.html">
<meta property="og:image" content="{URL}img/pzenos/card.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#03141A">
<link rel="icon" href="favicon.png">
<link rel="preload" href="fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{pz_img(PZ_HERO[0])}" as="image" fetchpriority="high">
<link rel="stylesheet" href="css/gate.css?v={VER}">
<link rel="stylesheet" href="css/zenos.css?v={VER}">
</head>
<body class="pz">
{gate("full")}
<script>try{{if(sessionStorage.getItem("pz-nav")!=="zenos")document.getElementById("pz-gate").className="pz-gate intro"}}catch(e){{}}</script>
<a class="skip" href="#main">Skip to content</a>
<div class="pz-sea" aria-hidden="true"></div>
<div class="pz-watermark" aria-hidden="true">{EMBLEM}</div>
<header class="pz-top">
  <div class="wrap">
    <a class="pz-brand" href="#top">{EMBLEM}{letters("P_ZENOS")}</a>
    <button class="menu-btn" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
    <nav class="nav">
      <a href="#story">Story</a>
      <a href="#windows">Windows</a>
      <a href="#videos">Videos</a>
      <a href="#photos">Photos</a>
      {ext(PATREON, "Patreon", "pz-btn")}
      <a class="pz-back" href="index.html" data-jamzey><img src="img/mark.webp" alt="" width="18" height="22">Jamzey St.</a>
    </nav>
  </div>
</header>

<main id="main">
<section class="pz-hero" id="top">
  <div class="pz-slides">{slides}</div>
  <div class="pz-hero-in">
    <span class="pz-kicker" style="--d:0">A Jamzey St. original · In development</span>
    <h1 style="--d:.1">{letters("P_ZENOS")}</h1>
    <p class="pz-slogan" style="--d:.55">{escape(PZ_SLOGAN)}</p>
    <div class="cta" style="--d:.75">{ext(PATREON, "Follow on Patreon", "pz-btn")}<a class="pz-ghost" href="#windows">Explore the windows</a></div>
  </div>
  <div class="pz-dots">{dots}</div>
  <span class="pz-scroll" aria-hidden="true"></span>
</section>

<section class="pz-story" id="story">
  <div class="wrap">
    <div class="pz-head" data-reveal>
      <span class="pz-kicker">Chapter one</span>
      <h2>The one that <em>started it all</em></h2>
      <p>Before the snow, the rain and the fire, there was P_Zenos: my own cinematic third-person action-adventure,
        built in Unity 6 with HDRP and ray tracing. It's the project Jamzey St. began with.</p>
      <p>Every swim, climb, boat ride and explosion on this page is a real-time shot from the game. It's still in
        development, and you can follow every step of it on Patreon.</p>
      <div class="pz-stats">{stats}</div>
    </div>
    <figure class="pz-frame" data-reveal><img src="{pz_img(PZ_STORY_SHOT)}" alt="{escape(PZ_SHOTS[PZ_STORY_SHOT])}" width="1920" height="1080" loading="lazy" decoding="async"><figcaption>P_Zenos · {escape(PZ_SHOTS[PZ_STORY_SHOT])}</figcaption></figure>
  </div>
</section>

<section id="windows">
  <div class="wrap">
    <div class="pz-head" data-reveal>
      <span class="pz-kicker">Windows</span>
      <h2>Windows into <em>the world</em></h2>
      <p>Pick a window. Each one opens on a part of P_Zenos, captured in the editor.</p>
    </div>
    <div data-reveal>
      <div class="pz-tabs" role="tablist" aria-label="P_Zenos windows">{tabs}</div>{windows}
    </div>
  </div>
</section>

<section id="videos">
  <div class="wrap">
    <div class="pz-head" data-reveal>
      <span class="pz-kicker">Videos</span>
      <h2>See it <em>move</em></h2>
      <p>Devlogs and gameplay captures from P_Zenos.</p>
    </div>
    <div data-reveal>{videos}</div>
  </div>
</section>

<section id="photos">
  <div class="wrap">
    <div class="pz-head" data-reveal>
      <span class="pz-kicker">Photo mode</span>
      <h2>Every <em>shot</em></h2>
      <p>{len(PZ_SHOTS)} shots straight from the game. Click any of them to see it full size.</p>
    </div>
    <div class="gallery" data-reveal>{gallery}</div>
  </div>
</section>

<section class="pz-join">
  <div class="wrap" data-reveal>
    {EMBLEM}
    <h2>Be there <em>from the start</em></h2>
    <p>Devlogs, work-in-progress builds and behind-the-scenes breakdowns of P_Zenos land on Patreon first.</p>
    <div class="cta">{ext(PATREON, "Join on Patreon", "pz-btn")}{ext(YOUTUBE, "YouTube", "pz-ghost")}<a class="pz-ghost" href="index.html" data-jamzey>Jamzey St. tools</a></div>
  </div>
</section>
</main>
<dialog class="lightbox">
  <img alt="">
  <p></p>
  <button class="lb-btn lb-prev" aria-label="Previous">‹</button>
  <button class="lb-btn lb-next" aria-label="Next">›</button>
  <button class="lb-btn lb-close" aria-label="Close">✕</button>
</dialog>
<footer class="pz-foot">
  <div class="wrap">
    <a class="pz-brand" href="#top">{EMBLEM}{letters("P_ZENOS")}</a>
    <span>A Jamzey St. project</span>
    <nav>{ext(PATREON, "Patreon")}{ext(YOUTUBE, "YouTube")}<a href="index.html" data-jamzey>Jamzey St.</a><a href="mailto:{EMAIL}">{EMAIL}</a></nav>
    <p class="fine">© 2026 Jamzey St. All screenshots are real-time captures from P_Zenos in development. Unity is a trademark of Unity Technologies; this site is not affiliated with Unity.</p>
  </div>
</footer>
<script src="js/site.js?v={VER}"></script>
<script src="js/gate.js?v={VER}"></script>
<script src="js/zenos.js?v={VER}"></script>{f'''
<script data-goatcounter="https://{GOATCOUNTER}.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>''' if GOATCOUNTER else ""}
</body>
</html>
"""

def write(name, html):
    open(os.path.join(SITE, name), "w", encoding="utf-8", newline="\n").write(html)

write("index.html", index())
for a in ASSETS:
    write(f"{a['slug']}.html", product(a))
write("pzenos.html", zenos())
print("built", 2 + len(ASSETS), "pages")
