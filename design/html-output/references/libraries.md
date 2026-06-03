# Library / CDN decision matrix

Default: **self-contained**. Only reach for a CDN when the alternative is materially worse (illegible hand-rolled SVG, no charting at all, etc).

## Decision table

| Need | Self-contained answer | CDN answer | Recommendation |
|------|----------------------|-----------|----------------|
| Flowchart, sequence, state, mind map, gantt | Hand-rolled SVG (tedious) | Mermaid | **Mermaid** — quality gain is huge |
| Bar / line / pie / scatter chart with axes and ticks | Static SVG bar chart | Chart.js | **Chart.js** — anything beyond 5 data points |
| Single sparkline or trend line | Inline SVG path | Chart.js | **Self-contained SVG** |
| Custom diagram (e.g. layered architecture) | Inline SVG | n/a | **Self-contained SVG** |
| Interactive table sort / filter | Vanilla JS click handlers | DataTables, AG Grid | **Vanilla JS** for ≤50 rows; CDN only for richer needs |
| Syntax-highlighted code blocks | Plain `<pre>` with classes | Prism, Highlight.js | **Plain `<pre>`** unless code is the central artifact |
| Math / equations | n/a | KaTeX | **KaTeX** if math is present |
| 3D / WebGL | n/a | Three.js | **Three.js** — never roll your own |

## Approved CDN snippets

When you do use a CDN, use these exact tags. They live in `assets/snippets/`.

### Mermaid (diagrams)
```html
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<script>
  mermaid.initialize({
    startOnLoad: true,
    theme: 'base',
    themeVariables: {
      primaryColor: '#1E3A2F',
      primaryTextColor: '#F4F1EB',
      primaryBorderColor: '#1E3A2F',
      lineColor: '#4A5568',
      secondaryColor: '#E0D8C8',
      tertiaryColor: '#E8A838',
      fontFamily: 'Inter, system-ui, sans-serif'
    }
  });
</script>
```
Diagram blocks use `<pre class="mermaid">...</pre>` (not `<code>`).

### Chart.js (charts)
```html
<script src="https://cdn.jsdelivr.net/npm/chart.js@4"></script>
```
Default colors to pass into datasets:
- Primary fill: `#1E3A2F`
- Accent fill: `#E8A838`
- Secondary fill: `#E0D8C8`
- Gridlines / axes: `rgba(74, 85, 104, 0.2)`

### KaTeX (math)
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
        onload="renderMathInElement(document.body);"></script>
```

## Banned / avoid

- jQuery — pure vanilla JS works for everything we need.
- Bootstrap, Bulma, generic CSS frameworks — they fight the brand tokens.
- Tailwind via CDN — debatable, but the brand-tokens block already gives utility-shaped classes for the patterns we use; adding Tailwind doubles the cognitive load. Skip unless the user explicitly asks.
- Webfonts beyond Inter + Space Grotesk.
- Analytics, tracking, telemetry — never include them in an artifact.
