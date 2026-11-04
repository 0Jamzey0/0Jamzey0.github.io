"""Generates index.html and one page per asset. Edit the data below, then: python tools/build.py"""
import hashlib, os
from html import escape

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VER = hashlib.sha1(b"".join(open(os.path.join(SITE, f), "rb").read()
                            for f in ("css/style.css", "js/site.js", "js/grid.js"))).hexdigest()[:8]
URL = "https://0jamzey0.github.io/"
STORE = "https://assetstore.unity.com/publishers/100637"
YOUTUBE = "https://www.youtube.com/@Jamzey-Dev"
PATREON = "https://www.patreon.com/cw/JamzeyDev"
EMAIL = "jamzeyst@gmail.com"

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
        slug="downpour", name="Downpour", sub="Rain & Wet Surfaces for HDRP",
        store="https://assetstore.unity.com/packages/package/415192", version="1.0.0",
        pipelines=["HDRP"],
        tag="Rain-soaked scenes without touching a single material.",
        lead="Streets darken and gloss, puddles fill the low spots, drops run down walls, glass and cars, eaves drip, "
             "and everything under a roof stays dry. It works through HDRP Custom Passes, so it applies to every "
             "object whatever shader it uses.",
        videos=[("Shq2jn_EiPQ", "Downpour trailer", "Rain & wet surfaces for HDRP")],
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
        gallery=[("01_hero", "Downpour hero street"), ("02_before_after", "Dry and wet, before and after"),
                 ("04_puddles", "Puddles with ripples"), ("07_running_drops", "Running drops"),
                 ("09_glass", "Drops on glass"), ("11_shelter", "Dry under shelter"),
                 ("14_lightning", "Lightning"), ("19_presets", "Weather presets")],
        specs=[("Unity", "6.0 LTS or newer"), ("Render pipeline", "HDRP 17.0+"),
               ("Approach", "Custom Passes, no material changes"), ("Version", "1.0.0"),
               ("Demo scenes", "Showcase street + minimal"), ("Content", "100% original")],
    ),
    dict(
        slug="carve", name="Carve", sub="Silhouette Parallax Occlusion Mapping for HDRP & URP",
        store="https://assetstore.unity.com/packages/package/418204", version="1.0.0",
        pipelines=["HDRP", "URP"],
        tag="Real depth on flat surfaces, with carved outlines and true intersections.",
        lead="Parallax occlusion mapping built to hold up where classic POM falls apart: mesh edges are carved into "
             "the shape of the relief, props meet it at its true depth, and light, shadows and reflections follow "
             "every crack. One package for HDRP and URP.",
        videos=[("LmxFYLq_1uU", "Carve trailer", "Silhouette POM for HDRP & URP")],
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
               ("Materials", "13 included"), ("Version", "1.0.0"),
               ("Demo scenes", "3 per pipeline"), ("Content", "100% original")],
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
    dict(slug="scorch", name="Scorch", sub="Dynamic Fire & Burn System for HDRP", pipelines=["HDRP"],
         status="Coming soon",
         tag="Fire that spreads, chars and burns through any object, without changing its materials."),
    dict(slug="dustfall", name="Dustfall", sub="Sand, Dust & Sandstorms for HDRP", pipelines=["HDRP"],
         status="In development",
         tag="Sand that takes footprints and tire tracks, dust on every surface, and towering sandstorms."),
    dict(slug="amberfall", name="Amberfall", sub="Autumn Leaves & Seasonal Foliage for HDRP & URP",
         pipelines=["HDRP", "URP"], status="In development",
         tag="Autumn leaves that fall, gather and drift through your scenes as the season turns."),
]

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
<link rel="icon" href="favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css?v={VER}">
</head>
<body>
<header class="top">
  <div class="wrap">
    <a class="brand" href="index.html"><img src="img/mark.png" alt="" width="28" height="34">Jamzey St.</a>
    <button class="menu-btn" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
    <nav class="nav">
      <a href="index.html#assets">Assets</a>
      <a href="index.html#videos">Videos</a>
      <a href="index.html#about">About</a>
      <a href="{PATREON}" target="_blank" rel="noopener">Patreon</a>
      <a class="btn btn-primary btn-small" href="{STORE}" target="_blank" rel="noopener">Asset Store</a>
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
      <a class="brand" href="index.html"><img src="img/mark.png" alt="" width="28" height="34">Jamzey St.</a>
      <p class="blurb">Weather, surface and VFX tools for Unity. Built and tested in Unity 6.</p>
    </div>
    <div>
      <h4>Assets</h4>
      <ul>{"".join(f'<li><a href="{a["slug"]}.html">{a["name"]}</a></li>' for a in ASSETS)}</ul>
    </div>
    <div>
      <h4>Find me</h4>
      <ul>
        <li><a href="{STORE}" target="_blank" rel="noopener">Unity Asset Store</a></li>
        <li><a href="{YOUTUBE}" target="_blank" rel="noopener">YouTube</a></li>
        <li><a href="{PATREON}" target="_blank" rel="noopener">Patreon</a></li>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
      </ul>
    </div>
    <p class="fine">© 2026 Jamzey St. Unity is a trademark of Unity Technologies; this site is not affiliated with Unity.</p>
  </div>
</footer>
<script src="js/site.js?v={VER}"></script>
<script src="js/grid.js?v={VER}"></script>
</body>
</html>
"""

def video(vid, title, note):
    cap = f'<figcaption>{escape(title)}<small>{escape(note)}</small></figcaption>'
    if vid.endswith(".mp4"):
        poster = "img/" + vid.split("/")[1].replace("-trailer.mp4", "") + "/card.jpg"
        return (f'<figure class="video"><div class="yt-frame"><video controls preload="none" playsinline '
                f'poster="{poster}" aria-label="{escape(title)}"><source src="{vid}" type="video/mp4"></video></div>{cap}</figure>')
    return (f'<figure class="video"><button class="yt" data-id="{vid}" aria-label="Play {escape(title)}">'
            f'<span class="play"></span></button>{cap}</figure>')

def card(a):
    return f"""<a class="card" href="{a['slug']}.html">
  <div class="shot">{f'<span class="status">{a["status"]}</span>' if a.get("status") else ""}<img src="img/{a['slug']}/card.jpg" alt="{a['name']}" loading="lazy" width="960" height="540"></div>
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
    vids = [v for a in sorted(ASSETS, key=lambda a: bool(a["store"])) for v in a["videos"]]
    live = sum(1 for a in ASSETS if a["store"])
    return head("Jamzey St. · Weather, surfaces & VFX for Unity",
                "Drop-in environment tools for Unity: deformable snow, rain and wet surfaces, and silhouette "
                "parallax occlusion mapping for HDRP and URP.") + f"""
<main>
<section class="hero">
  <img class="blocks blocks-left" src="img/blocks-left.svg" alt="">
  <img class="blocks blocks-right" src="img/blocks-right.svg" alt="">
  <div class="wrap">
    <span class="eyebrow">Jamzey St.</span>
    <h1>Weather, surfaces <em>&amp;</em> VFX</h1>
    <p class="lead">Drop-in environment tools for Unity. Snow that takes footprints, rain that soaks every surface,
      and relief with real depth, all working on any shader with no material changes.</p>
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

<section id="upcoming" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head">
      <div><div class="kicker">In the workshop</div><h2>Coming <em>next</em></h2></div>
      <p>Fire, sand and autumn leaves are on the bench. Patreon members see them first.</p>
    </div>
    <div class="cards">
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
        footprints, rain that soaks surfaces, and surfaces with real depth.</p>
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
      <p>Work-in-progress builds, behind-the-scenes breakdowns and early looks at upcoming assets.</p>
    </div>
    <div class="cta" style="display:flex;gap:12px;flex-wrap:wrap">
      <a class="btn" href="{PATREON}" target="_blank" rel="noopener">Join on Patreon</a>
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
<main>
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
    <div class="shot"><img src="img/{a['slug']}/{a.get('hero', a['gallery'][0][0])}.jpg" alt="{escape(a['name'] + ' – ' + a['sub'])}" width="1600" height="900"></div>
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
{"".join(f'<div class="feature"><h3>{escape(t)}</h3><ul>{"".join(f"<li>{escape(x)}</li>" for x in items)}</ul></div>' for t, items in a['features'])}
    </div>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="sec-head"><div><div class="kicker">Gallery</div><h2>Screenshots</h2></div><p>Click any shot to view it full size.</p></div>
    <div class="gallery">
{"".join(f'<button data-full="img/{a["slug"]}/{f}.jpg"><img src="img/{a["slug"]}/{f}_thumb.jpg" alt="{escape(alt)}" loading="lazy" width="640" height="360"></button>' for f, alt in a['gallery'])}
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
    <div class="cards">
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

def write(name, html):
    open(os.path.join(SITE, name), "w", encoding="utf-8", newline="\n").write(html)

write("index.html", index())
for a in ASSETS:
    write(f"{a['slug']}.html", product(a))
print("built", 1 + len(ASSETS), "pages")
