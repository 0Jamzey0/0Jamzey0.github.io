// The P_Zenos gate: animated hand-over between Jamzey St. and P_Zenos (runs on every page)
(() => {
  const root = document.documentElement;
  const still = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const KEY = "pz-nav";
  const store = v => { try { v ? sessionStorage.setItem(KEY, v) : sessionStorage.removeItem(KEY); } catch (e) {} };
  const go = (href, flag) => { store(flag); location.href = href; };
  const plain = e => e.button === 0 && !e.metaKey && !e.ctrlKey && !e.shiftKey && !e.altKey;
  const BRAND = "Jamzey St.";

  // Arriving on Jamzey St. from P_Zenos: gate.css paints the curtain at first paint; lift it.
  if (root.classList.contains("jz-arrive")) {
    store(null);
    if (still) root.classList.remove("jz-arrive");
    else setTimeout(() => {
      root.classList.add("jz-reveal");
      setTimeout(() => root.classList.remove("jz-arrive", "jz-reveal"), 1600);
    }, 220);
  }

  // Letters shuffle, then settle left to right into the new word
  const scramble = (el, to, ms) => {
    const from = el.textContent, len = Math.max(from.length, to.length);
    const pool = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_#/*+<>";
    const t0 = performance.now();
    const step = now => {
      const p = Math.min((now - t0) / ms, 1);
      let s = "";
      for (let i = 0; i < len; i++) {
        if (p > .3 + .6 * i / len) s += to[i] || "";
        else s += p < .08 ? (from[i] || "") : pool[Math.random() * pool.length | 0];
      }
      el.textContent = s;
      if (p < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };
  const brandText = () => {
    const brand = document.querySelector(".top .brand");
    if (!brand) return null;
    let span = brand.querySelector(".brand-txt");
    if (!span) {
      const node = [...brand.childNodes].find(n => n.nodeType === 3 && n.textContent.trim());
      if (!node) return null;
      span = document.createElement("span");
      span.className = "brand-txt";
      span.textContent = node.textContent;
      node.replaceWith(span);
    }
    return span;
  };

  let leaving = false;
  const toZenos = href => {
    const tpl = document.getElementById("pz-gate-tpl");
    if (still || !tpl) return go(href, "zenos");
    if (leaving) return;
    leaving = true;
    new Image().src = "img/pzenos/05.webp";   // the first hero slide, so it is ready when the water drains
    root.classList.add("pz-leaving");
    const txt = brandText();
    if (txt) scramble(txt, "P_ZENOS", 1100);
    const gate = tpl.content.firstElementChild.cloneNode(true);
    gate.classList.add("rise");
    gate.addEventListener("click", () => go(href, "zenos"));
    document.body.append(gate);
    setTimeout(() => go(href, "zenos"), 2600);
  };

  const toJamzey = href => {
    if (still) return go(href, "jamzey");
    if (leaving) return;
    leaving = true;
    root.classList.add("jz-leaving");
    let dark = false;
    try { dark = localStorage.getItem("theme") === "dark"; } catch (e) {}
    const g = document.createElement("div");
    g.className = "jz-gate" + (dark ? " dark" : "");
    g.setAttribute("aria-hidden", "true");
    g.innerHTML = '<img src="img/mark.webp" alt="" width="76" height="92"><div>' +
      [...BRAND].map((c, i) => `<span style="--i:${i}">${c}</span>`).join("") + "</div>";
    document.body.append(g);
    setTimeout(() => go(href, "jamzey"), 1500);
  };

  document.addEventListener("click", e => {
    const a = e.target.closest("a[data-zenos], a[data-jamzey]");
    if (!a || !plain(e) || a.target === "_blank") return;
    e.preventDefault();
    a.hasAttribute("data-zenos") ? toZenos(a.href) : toJamzey(a.href);
  });

  // Warm up P_Zenos as soon as someone shows interest in it
  let warmed = false;
  const warm = e => {
    if (warmed || !e.target.closest?.("a[data-zenos]")) return;
    warmed = true;
    const l = document.createElement("link");
    l.rel = "prefetch"; l.href = "pzenos.html";
    document.head.append(l);
    new Image().src = "img/pzenos/05.webp";
  };
  document.addEventListener("pointerover", warm, { passive: true });
  document.addEventListener("focusin", warm);

  // Coming back with the browser's Back button restores a frozen page: undo the transition
  addEventListener("pageshow", e => {
    if (!e.persisted) return;
    leaving = false;
    root.classList.remove("pz-leaving", "jz-leaving", "jz-arrive", "jz-reveal");
    document.querySelectorAll(".pz-gate.rise, .jz-gate").forEach(n => n.remove());
    const txt = document.querySelector(".top .brand .brand-txt");
    if (txt) txt.textContent = BRAND;
  });
})();
