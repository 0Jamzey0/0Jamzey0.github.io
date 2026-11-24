# Jamzey St. portfolio

Static site for https://0jamzey0.github.io/, served by GitHub Pages from `main`.

- Page content lives in `tools/build.py`; edit it, then run `python tools/build.py` to regenerate the HTML.
- `tools/prepare_media.py` copies and resizes gallery images from `D:/StoreAssetProjects_Media/Publishing`.
- `tools/blocks.py` draws the isometric brand blocks as SVG.

- After prepare_media.py, run python tools/to_webp.py to make the WebP versions the pages use (the JPG card/social files stay for link previews), then python tools/build.py.
- Fonts are self-hosted in onts/.
