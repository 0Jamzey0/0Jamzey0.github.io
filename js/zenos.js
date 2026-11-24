// P_Zenos page: gate reveal, hero slideshow, windows, scroll reveals
(() => {
  const body = document.body;
  const still = matchMedia("(prefers-reduced-motion: reduce)").matches;
  try { sessionStorage.removeItem("pz-nav"); } catch (e) {}

  // ---- the gate: drain the water ----
  let started = false;
  const begin = () => { if (started) return; started = true; body.classList.add("pz-ready"); startSlides(); };
  const gate = document.getElementById("pz-gate");
  if (!gate || still) { gate?.remove(); setTimeout(begin); }
  else {
    let drained = false;
    const drain = () => {
      if (drained) return;
      drained = true;
      gate.classList.remove("full", "intro");
      gate.classList.add("drain");
      setTimeout(begin, 380);
      setTimeout(() => gate.remove(), 1400);
    };
    // arrived through the gate: hold the title for a beat; a direct visit plays the intro first
    setTimeout(drain, gate.classList.contains("intro") ? 2300 : 380);
    gate.addEventListener("click", drain);
    addEventListener("keydown", drain, { once: true });
  }

  // ---- header ----
  const top = document.querySelector(".pz-top");
  const onScroll = () => top?.classList.toggle("scrolled", scrollY > 40);
  addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // ---- hero slideshow ----
  const slides = [...document.querySelectorAll(".pz-slides img")];
  const dots = [...document.querySelectorAll(".pz-dots button")];
  const DUR = 6000;
  let cur = 0, timer = 0;
  function show(n) {
    slides[cur]?.classList.remove("on");
    cur = (n + slides.length) % slides.length;
    const next = slides[cur];
    if (next) { next.loading = "eager"; void next.offsetWidth; next.classList.add("on"); }
    dots.forEach((d, i) => { d.classList.remove("on"); d.classList.toggle("done", i < cur); d.setAttribute("aria-current", i === cur); });
    if (dots[cur]) { void dots[cur].offsetWidth; dots[cur].classList.add("on"); }
    clearTimeout(timer);
    if (!still && slides.length > 1) timer = setTimeout(() => show(cur + 1), DUR);
  }
  function startSlides() {
    if (!slides.length) return;
    document.documentElement.style.setProperty("--slide", DUR + "ms");
    slides[0].classList.remove("on");
    show(0);
    slides[1] && (slides[1].loading = "eager");
  }
  dots.forEach((d, i) => d.addEventListener("click", () => show(i)));
  document.addEventListener("visibilitychange", () => {
    if (document.hidden) clearTimeout(timer); else if (started) show(cur);
  });

  // ---- windows: tabs + picture switcher ----
  const tabs = [...document.querySelectorAll(".pz-tabs [role=tab]")];
  const select = t => tabs.forEach(x => {
    const on = x === t;
    x.setAttribute("aria-selected", on);
    x.tabIndex = on ? 0 : -1;
    document.getElementById(x.getAttribute("aria-controls")).hidden = !on;
  });
  tabs.forEach((t, i) => {
    t.addEventListener("click", () => select(t));
    t.addEventListener("keydown", e => {
      const d = { ArrowRight: 1, ArrowLeft: -1 }[e.key];
      if (!d) return;
      e.preventDefault();
      const n = tabs[(i + d + tabs.length) % tabs.length];
      select(n); n.focus();
    });
  });
  const pad = n => String(n).padStart(2, "0");
  document.querySelectorAll(".pz-window").forEach(w => {
    const view = w.querySelector(".pz-view"), count = w.querySelector(".pz-count");
    const thumbs = [...w.querySelectorAll(".pz-thumbs button")];
    thumbs.forEach((b, i) => b.addEventListener("click", () => {
      thumbs.forEach(x => x.setAttribute("aria-pressed", x === b));
      const img = new Image();
      img.src = b.dataset.full;
      img.alt = b.querySelector("img").alt;
      img.width = 1920; img.height = 1080;
      view.querySelector("img").replaceWith(img);
      if (count) count.textContent = `${pad(i + 1)} / ${pad(thumbs.length)}`;
    }));
  });

  // ---- "coming soon" video window: slow slideshow behind the message ----
  const soon = [...document.querySelectorAll(".pz-soon .pz-view img")];
  if (soon.length > 1 && !still) {
    let k = 0;
    setInterval(() => { soon[k].classList.remove("on"); k = (k + 1) % soon.length; soon[k].classList.add("on"); }, 3200);
  }

  // ---- reveal sections as they scroll in ----
  const items = document.querySelectorAll("[data-reveal]");
  if ("IntersectionObserver" in window && !still) {
    const io = new IntersectionObserver(es => es.forEach(en => {
      if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
    }), { threshold: .12 });
    items.forEach(n => io.observe(n));
  } else items.forEach(n => n.classList.add("in"));
})();
