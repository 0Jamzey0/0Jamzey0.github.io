(() => {
  const STEP = 32, SLOPE = Math.tan(Math.PI / 6);
  const SIGMA = 130, PUSH = 46, GLOW = 240;
  const HALF = STEP / 2 / SLOPE;
  const still = matchMedia("(prefers-reduced-motion: reduce)").matches;

  document.querySelectorAll(".hero, .p-hero").forEach(host => {
    const canvas = document.createElement("canvas");
    canvas.className = "grid-canvas";
    canvas.setAttribute("aria-hidden", "true");
    host.prepend(canvas);
    host.classList.add("live-grid");
    const ctx = canvas.getContext("2d");
    const fade = host.classList.contains("hero");
    let W = 0, H = 0, dpr = 1;
    const target = { x: 0, y: 0, s: 0 }, cur = { x: 0, y: 0, s: 0 };
    let raf = 0;

    const warp = (x, y) => {
      if (cur.s < .001) return [x, y];
      const dx = x - cur.x, dy = y - cur.y, r = Math.hypot(dx, dy);
      if (r < .01 || r > SIGMA * 3) return [x, y];
      const k = PUSH * cur.s * Math.exp(-(r * r) / (SIGMA * SIGMA)) / r;
      return [x + dx * k, y + dy * k];
    };

    const lines = () => {
      ctx.beginPath();
      for (const dir of [1, -1]) {
        const lo = dir > 0 ? -SLOPE * W : 0, hi = dir > 0 ? H : H + SLOPE * W;
        for (let c = Math.floor(lo / STEP) * STEP; c <= hi; c += STEP) {
          const near = cur.s > .001 &&
            Math.abs(cur.y - (dir * SLOPE * cur.x + c)) / Math.hypot(1, SLOPE) < SIGMA * 3;
          const dx = near ? 5 : Math.max(W, 1);
          for (let x = 0; x <= W + dx - 1; x += dx) {
            const xx = Math.min(x, W), [px, py] = warp(xx, dir * SLOPE * xx + c);
            x === 0 ? ctx.moveTo(px, py) : ctx.lineTo(px, py);
          }
        }
      }
    };

    const draw = () => {
      if (W < 1 || H < 1) return;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      ctx.clearRect(0, 0, W, H);
      ctx.globalCompositeOperation = "source-over";
      ctx.lineWidth = 1;
      ctx.strokeStyle = "rgba(22, 21, 20, .08)";
      lines();
      ctx.stroke();
      if (fade) {
        ctx.save();
        ctx.globalCompositeOperation = "destination-out";
        ctx.translate(W / 2, H / 2);
        ctx.scale(W * .5, H * .6);
        const g = ctx.createRadialGradient(0, 0, 0, 0, 0, 1);
        g.addColorStop(0, "rgba(0,0,0,1)");
        g.addColorStop(.6, "rgba(0,0,0,.85)");
        g.addColorStop(1, "rgba(0,0,0,0)");
        ctx.fillStyle = g;
        ctx.fillRect(-1, -1, 2, 2);
        ctx.restore();
      }
      if (cur.s > .001) {
        const g = ctx.createRadialGradient(cur.x, cur.y, 0, cur.x, cur.y, GLOW);
        g.addColorStop(0, `rgba(226, 94, 34, ${.9 * cur.s})`);
        g.addColorStop(1, "rgba(226, 94, 34, 0)");
        ctx.strokeStyle = g;
        ctx.lineWidth = 1.6;
        lines();
        ctx.stroke();
        ctx.fillStyle = "#E25E22";
        const k0 = Math.floor((cur.x - GLOW) / HALF), k1 = Math.ceil((cur.x + GLOW) / HALF);
        const m0 = Math.floor((cur.y - GLOW) / (STEP / 2)), m1 = Math.ceil((cur.y + GLOW) / (STEP / 2));
        for (let k = k0; k <= k1; k++) {
          for (let m = m0; m <= m1; m++) {
            if ((k + m) & 1) continue;
            const x = k * HALF, y = m * STEP / 2;
            const t = 1 - Math.hypot(x - cur.x, y - cur.y) / GLOW;
            if (t <= 0) continue;
            const [px, py] = warp(x, y);
            ctx.globalAlpha = t * cur.s;
            ctx.beginPath();
            ctx.arc(px, py, 1 + 2.2 * t, 0, Math.PI * 2);
            ctx.fill();
          }
        }
        ctx.globalAlpha = 1;
      }
    };

    const tick = () => {
      cur.x += (target.x - cur.x) * .18;
      cur.y += (target.y - cur.y) * .18;
      cur.s += (target.s - cur.s) * .1;
      draw();
      const settled = Math.abs(target.x - cur.x) < .3 && Math.abs(target.y - cur.y) < .3 &&
        Math.abs(target.s - cur.s) < .002;
      raf = settled ? 0 : requestAnimationFrame(tick);
      if (settled) { cur.s = target.s; draw(); }
    };
    const kick = () => { if (!raf) raf = requestAnimationFrame(tick); };

    const resize = () => {
      dpr = Math.min(devicePixelRatio || 1, 2);
      W = host.clientWidth; H = host.clientHeight;
      canvas.width = Math.round(W * dpr); canvas.height = Math.round(H * dpr);
      draw();
    };
    resize();
    new ResizeObserver(resize).observe(host);

    if (still) return;
    host.addEventListener("pointermove", e => {
      const r = host.getBoundingClientRect();
      target.x = e.clientX - r.left; target.y = e.clientY - r.top;
      if (cur.s < .01) { cur.x = target.x; cur.y = target.y; }
      target.s = 1;
      kick();
    });
    host.addEventListener("pointerleave", () => { target.s = 0; kick(); });
  });
})();
