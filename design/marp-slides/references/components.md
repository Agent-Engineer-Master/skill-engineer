# MARP Components Reference

## Table of contents
1. [Dashboard components](#dashboard-components)
2. [SVG charts](#svg-charts)
3. [Layout components](#layout-components)
4. [Interactive elements](#interactive-elements)
5. [Images](#images)
6. [SVG icons](#svg-icons)
7. [Animations](#animations)

---

## Dashboard components

### Metric card (gradient top border)
```html
<div style="background:var(--card); border:1px solid var(--border); border-radius:10px; padding:20px; position:relative; overflow:hidden;">
  <div style="position:absolute; top:0; left:0; right:0; height:2px; background:linear-gradient(90deg, var(--accent), transparent);"></div>
  <div style="font-size:0.55em; color:var(--label); text-transform:uppercase; letter-spacing:0.12em;">Revenue</div>
  <div style="font-size:2.2em; font-family:'Outfit'; font-weight:800; color:var(--light); margin:4px 0;">$42,800</div>
  <div style="font-size:0.7em; color:var(--green);">↑ 12.4% vs last month</div>
</div>
```

### Status dots
```html
<!-- green = active, yellow = learning/review, red = paused/error -->
<svg width="8" height="8" viewBox="0 0 8 8"><circle cx="4" cy="4" r="4" fill="#22c55e"/></svg>
<svg width="8" height="8" viewBox="0 0 8 8"><circle cx="4" cy="4" r="4" fill="#f5a623"/></svg>
<svg width="8" height="8" viewBox="0 0 8 8"><circle cx="4" cy="4" r="4" fill="#ef4444"/></svg>
```

### Verdict tags
```html
<span class="tag" style="background:#22c55e12; color:var(--green); border:1px solid #22c55e22;">Scale</span>
<span class="tag" style="background:#ef444412; color:var(--red); border:1px solid #ef444422;">Kill</span>
<span class="tag" style="background:#f5a62312; color:var(--yellow); border:1px solid #f5a62322;">Review</span>
```

### Hover rows
```html
<div class="row" style="padding:10px 12px; display:flex; justify-content:space-between; align-items:center;">
  <span style="color:var(--body); font-size:0.75em;">Row label</span>
  <span style="color:var(--light); font-family:'Outfit'; font-weight:600;">Value</span>
</div>
```

---

## SVG charts

**Critical:** Use `preserveAspectRatio="xMidYMid meet"` for inline charts. For image backgrounds: always `contain`, never `cover` (cover mode crops edges).

### Line / area chart
```html
<svg viewBox="0 0 900 240" preserveAspectRatio="xMidYMid meet" style="width:100%;">
  <defs>
    <linearGradient id="areaGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#ff6b1a" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#ff6b1a" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <!-- Grid lines -->
  <line x1="0" y1="60" x2="900" y2="60" stroke="#1a1a1a" stroke-width="1"/>
  <line x1="0" y1="120" x2="900" y2="120" stroke="#1a1a1a" stroke-width="1"/>
  <line x1="0" y1="180" x2="900" y2="180" stroke="#1a1a1a" stroke-width="1"/>
  <!-- Area fill -->
  <polygon points="0,180 150,140 300,100 450,120 600,60 750,80 900,40 900,240 0,240" fill="url(#areaGrad)"/>
  <!-- Line -->
  <polyline points="0,180 150,140 300,100 450,120 600,60 750,80 900,40" fill="none" stroke="#ff6b1a" stroke-width="2.5"/>
  <!-- Data points -->
  <circle cx="600" cy="60" r="5" fill="#ff6b1a"/>
</svg>
```

### Donut chart
Math: circumference for radius r = 2 × π × r. For r=110: circ ≈ 691. Each segment = (pct/100) × 691. Offsets accumulate negatively. Always `transform="rotate(-90 cx cy)"`.
```html
<svg viewBox="0 0 240 240" style="width:180px;">
  <!-- Background ring -->
  <circle cx="120" cy="120" r="90" fill="none" stroke="#111" stroke-width="28"/>
  <!-- Segment: 65% orange -->
  <circle cx="120" cy="120" r="90" fill="none" stroke="#ff6b1a" stroke-width="28"
    stroke-dasharray="449 242" stroke-dashoffset="0" transform="rotate(-90 120 120)"/>
  <!-- Center label -->
  <text x="120" y="115" text-anchor="middle" fill="#fff" font-family="Outfit" font-weight="800" font-size="36">65%</text>
  <text x="120" y="140" text-anchor="middle" fill="#666" font-family="Raleway" font-size="13">conversion</text>
</svg>
```

### Donut ring (single value)
For radius r=74: circ=465. Offset = 465 - (465 × pct/100). Example 89%: offset=51.
```html
<svg viewBox="0 0 160 160" style="width:120px;">
  <circle cx="80" cy="80" r="74" fill="none" stroke="#111" stroke-width="12"/>
  <circle cx="80" cy="80" r="74" fill="none" stroke="#ff6b1a" stroke-width="12"
    stroke-dasharray="465" stroke-dashoffset="51" stroke-linecap="round" transform="rotate(-90 80 80)"/>
  <text x="80" y="87" text-anchor="middle" fill="#fff" font-family="Outfit" font-weight="800" font-size="28">89%</text>
</svg>
```

### Stacked bar (horizontal)
```html
<div style="display:flex; height:18px; border-radius:4px; overflow:hidden; width:100%;">
  <div style="width:45%; background:var(--accent);"></div>
  <div style="width:30%; background:#444;"></div>
  <div style="width:25%; background:#1a1a1a;"></div>
</div>
```

### Vertical bar chart
```html
<div style="display:flex; align-items:flex-end; gap:12px; height:140px;">
  <div style="flex:1; background:linear-gradient(180deg, var(--accent), #cc5515); border-radius:3px 3px 0 0; height:80%;"></div>
  <div style="flex:1; background:linear-gradient(180deg, var(--accent), #cc5515); border-radius:3px 3px 0 0; height:60%;"></div>
  <div style="flex:1; background:linear-gradient(180deg, var(--accent), #cc5515); border-radius:3px 3px 0 0; height:100%;"></div>
</div>
```

### Sparkline (inline mini)
```html
<svg width="50" height="16"><polyline points="0,14 8,12 16,10 24,8 50,2" fill="none" stroke="#22c55e" stroke-width="1.2"/></svg>
```

### Gauge / half-circle meter
```html
<svg viewBox="0 0 200 110" style="width:180px;">
  <!-- Background arc -->
  <path d="M 20 100 A 80 80 0 0 1 180 100" fill="none" stroke="#1a1a1a" stroke-width="16" stroke-linecap="round"/>
  <!-- Value arc (adjust stroke-dasharray for percentage) -->
  <path d="M 20 100 A 80 80 0 0 1 180 100" fill="none" stroke="#ff6b1a" stroke-width="16" stroke-linecap="round"
    stroke-dasharray="220" stroke-dashoffset="66"/>
  <text x="100" y="95" text-anchor="middle" fill="#fff" font-family="Outfit" font-weight="800" font-size="28">70</text>
</svg>
```

---

## Layout components

### Card row
```html
<div style="display:flex; gap:14px;">
  <div style="flex:1; background:var(--card); border:1px solid var(--border); border-radius:10px; padding:16px;">…</div>
  <div style="flex:1; background:var(--card); border:1px solid var(--border); border-radius:10px; padding:16px;">…</div>
</div>
```

### Before / after split
```html
<div style="display:flex; gap:20px;">
  <div style="flex:1; border-top:3px solid var(--red); padding-top:12px;"><!-- BEFORE content --></div>
  <div style="flex:1; border-top:3px solid var(--green); padding-top:12px;"><!-- AFTER content --></div>
</div>
```

### Terminal mockup
```html
<div style="background:#0a0a0a; border-radius:8px; overflow:hidden;">
  <div style="padding:8px 12px; display:flex; gap:6px;">
    <div style="width:10px; height:10px; border-radius:50%; background:#ef4444;"></div>
    <div style="width:10px; height:10px; border-radius:50%; background:#f5a623;"></div>
    <div style="width:10px; height:10px; border-radius:50%; background:#22c55e;"></div>
  </div>
  <div style="padding:12px 16px; font-family:'IBM Plex Mono',monospace; font-size:0.72em; color:#22c55e;">
    $ command goes here<span style="border-right:2px solid #22c55e;">&nbsp;</span>
  </div>
</div>
```

### Chat bubbles
```html
<!-- User (left) -->
<div style="display:flex; gap:10px; align-items:flex-start; margin-bottom:10px;">
  <div style="background:#1a1a1a; border-radius:0 10px 10px 10px; padding:10px 14px; font-size:0.75em; color:var(--body); max-width:70%;">User message</div>
</div>
<!-- Agent (right, orange-tinted) -->
<div style="display:flex; gap:10px; align-items:flex-start; justify-content:flex-end; margin-bottom:10px;">
  <div style="background:#ff6b1a18; border:1px solid #ff6b1a22; border-radius:10px 0 10px 10px; padding:10px 14px; font-size:0.75em; color:var(--body); max-width:70%;">Agent response</div>
</div>
```

### Timeline
```html
<div style="border-left:2px solid var(--border); padding-left:20px; margin-left:10px;">
  <div style="position:relative; margin-bottom:18px;">
    <div style="position:absolute; left:-26px; top:4px; width:10px; height:10px; border-radius:50%; background:var(--accent);"></div>
    <div style="font-size:0.6em; color:var(--label);">Q1 2026</div>
    <div style="font-size:0.8em; color:var(--light);">Event label</div>
  </div>
</div>
```

---

## Interactive elements (HTML preview + export only)

```html
<!-- Collapsible -->
<details><summary>Title</summary><p>Content</p></details>

<!-- Tooltip -->
<abbr title="Full explanation">TERM</abbr>

<!-- Slider -->
<input type="range" min="0" max="100" value="70" style="accent-color:var(--accent); width:200px;" />

<!-- Checkbox -->
<input type="checkbox" checked style="accent-color:var(--accent);" /> Label

<!-- Progress bar -->
<progress value="76" max="100" style="accent-color:var(--accent); width:100%;"></progress>
```

---

## Images

**Critical:** Use relative paths only — `./image.png`. Absolute paths break in Obsidian preview.

```markdown
<!-- Logo in header -->
header: '![w:100](./logo.png)'

<!-- Photo background, darkened -->
![bg brightness:0.15](https://unsplash.com/photo-ID?w=1400)

<!-- Split layout — image right -->
![bg right:35% brightness:0.2 blur:3px](./image.png)

<!-- Split layout — image left -->
![bg left:30%](./image.png)
```

CDN logos:
```html
<img src="https://cdn.jsdelivr.net/gh/homarr-labs/dashboard-icons/png/name.png" style="width:200px;" />
```

Centered inline image:
```html
<div style="display:flex; justify-content:center;">
  <img src="./image.png" style="border-radius:8px; border:1px solid var(--border); width:300px;" />
</div>
```

---

## SVG icons

Wrapper: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="1.5">`

Sizes: inline=16px, cards=44px, features=32px.

| Icon | Path |
|---|---|
| Dollar | `<path d="M12 2v20M17 5H9.5a3.5 3.5 0 1 0 0 7h5a3.5 3.5 0 1 1 0 7H6"/>` |
| Heartbeat | `<polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>` |
| Check (green) | `<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/>` — use stroke="#22c55e" |
| Arrow up (green) | `<polyline points="18 15 12 9 6 15"/>` — use stroke="#22c55e" |
| Arrow down (red) | `<polyline points="18 9 12 15 6 9"/>` — use stroke="#ef4444" |
| Clock | `<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>` |
| Lightning | `<path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/>` |
| Warning (yellow) | triangle path — use stroke="#f5a623" |
| Globe | `<circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>` |
| Lock | `<rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>` |

---

## Animations (HTML export + preview only)

```css
@keyframes float { 0%,100% { transform:translateY(0); } 50% { transform:translateY(-8px); } }
@keyframes glow { 0%,100% { box-shadow:0 0 10px var(--accent); } 50% { box-shadow:0 0 25px var(--accent); } }
@keyframes blink { 0%,100% { border-color:var(--accent); } 50% { border-color:transparent; } }
```

Stagger with delay: `animation: float 4s ease-in-out 0.5s infinite;`
