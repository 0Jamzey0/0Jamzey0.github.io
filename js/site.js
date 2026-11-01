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
