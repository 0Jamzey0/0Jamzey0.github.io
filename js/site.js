document.querySelector(".menu-btn")?.addEventListener("click", e => {
  const nav = document.querySelector(".nav");
  e.currentTarget.setAttribute("aria-expanded", nav.classList.toggle("open"));
});

document.querySelectorAll(".yt").forEach(btn => {
  btn.style.backgroundImage = `url(https://i.ytimg.com/vi/${btn.dataset.id}/hqdefault.jpg)`;
  btn.addEventListener("click", () => {
    const frame = document.createElement("div");
    frame.className = "yt-frame";
    const f = document.createElement("iframe");
    f.src = `https://www.youtube-nocookie.com/embed/${btn.dataset.id}?autoplay=1&rel=0`;
    f.allow = "autoplay; encrypted-media; picture-in-picture; fullscreen";
    f.allowFullscreen = true;
    f.title = btn.getAttribute("aria-label");
    frame.append(f);
    btn.replaceWith(frame);
  }, { once: true });
});

const lb = document.querySelector("dialog.lightbox");
if (lb) {
  const shots = [...document.querySelectorAll(".gallery button")];
  const img = lb.querySelector("img"), cap = lb.querySelector("p");
  let i = 0;
  const show = n => {
    i = (n + shots.length) % shots.length;
    img.src = shots[i].dataset.full;
    img.alt = cap.textContent = shots[i].querySelector("img").alt;
  };
  shots.forEach((b, n) => b.addEventListener("click", () => { show(n); lb.showModal(); }));
  lb.querySelector(".lb-prev").onclick = () => show(i - 1);
  lb.querySelector(".lb-next").onclick = () => show(i + 1);
  lb.querySelector(".lb-close").onclick = () => lb.close();
  lb.addEventListener("click", e => { if (e.target === lb) lb.close(); });
  document.addEventListener("keydown", e => {
    if (!lb.open) return;
    if (e.key === "ArrowLeft") show(i - 1);
    if (e.key === "ArrowRight") show(i + 1);
  });
}

(() => {
  const btn = document.querySelector(".theme-toggle");
  if (!btn) return;
  const root = document.documentElement;
  const meta = document.querySelector('meta[name="theme-color"]');
  const still = matchMedia("(prefers-reduced-motion: reduce)");

  const sync = () => {
    const dark = root.dataset.theme === "dark";
    btn.setAttribute("aria-pressed", dark);
    btn.title = dark ? "Switch to light mode" : "Switch to night mode";
    if (meta) meta.content = dark ? "#141312" : "#E9E7DA";
  };
  const apply = dark => {
    if (dark) root.dataset.theme = "dark"; else delete root.dataset.theme;
    try { localStorage.setItem("theme", dark ? "dark" : "light"); } catch (e) {}
    sync();
  };
  sync();

  btn.addEventListener("click", () => {
    const dark = root.dataset.theme !== "dark";
    if (still.matches) return apply(dark);
    if (!document.startViewTransition) {
      root.classList.add("theme-fade");
      apply(dark);
      setTimeout(() => root.classList.remove("theme-fade"), 500);
      return;
    }
    const r = btn.getBoundingClientRect();
    const x = r.left + r.width / 2, y = r.top + r.height / 2;
    const end = Math.hypot(Math.max(x, innerWidth - x), Math.max(y, innerHeight - y));
    document.startViewTransition(() => apply(dark)).ready.then(() => {
      root.animate({ clipPath: [`circle(0px at ${x}px ${y}px)`, `circle(${end}px at ${x}px ${y}px)`] },
        { duration: 700, easing: "cubic-bezier(.65, 0, .35, 1)", pseudoElement: "::view-transition-new(root)" });
    });
  });
})();
