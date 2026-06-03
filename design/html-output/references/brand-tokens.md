# Brand Tokens — drop-in `<style>` block

Always paste this block as the very first thing inside `<style>` in every HTML output. It defines the brand palette, typography, spacing scale, base reset, and print rules.

## The block

```html
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;700&display=swap');

  :root {
    /* Palette — Antony Evans personal brand */
    --brand-primary:        #1E3A2F;   /* Forest green — headers, key elements */
    --brand-primary-rgb:    30, 58, 47;
    --brand-bg:             #F4F1EB;   /* Off-white — page background */
    --brand-bg-2:           #E0D8C8;   /* Warm tan — card backgrounds, depth */
    --brand-accent:         #E8A838;   /* Warm amber — CTAs, highlights, pull quotes */
    --brand-text:           #4A5568;   /* Slate — body text */
    --brand-white:          #FFFFFF;
    --brand-rule:           rgba(30, 58, 47, 0.12);

    /* Typography */
    --font-display: 'Space Grotesk', system-ui, -apple-system, sans-serif;
    --font-body:    'Inter', system-ui, -apple-system, sans-serif;
    --font-mono:    'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace;

    /* Spacing scale */
    --s-1: 0.25rem;
    --s-2: 0.5rem;
    --s-3: 1rem;
    --s-4: 1.5rem;
    --s-5: 2rem;
    --s-6: 3rem;
    --s-7: 4rem;

    /* Radii + shadow */
    --radius-sm: 4px;
    --radius-md: 8px;
    --radius-lg: 16px;
    --shadow-card: 0 1px 2px rgba(30, 58, 47, 0.06), 0 4px 12px rgba(30, 58, 47, 0.04);
  }

  *, *::before, *::after { box-sizing: border-box; }
  html, body { margin: 0; padding: 0; }

  body {
    background: var(--brand-bg);
    color: var(--brand-text);
    font-family: var(--font-body);
    font-size: 16px;
    line-height: 1.6;
    -webkit-font-smoothing: antialiased;
  }

  h1, h2, h3, h4 {
    font-family: var(--font-display);
    color: var(--brand-primary);
    line-height: 1.2;
    margin: 0 0 var(--s-3);
    font-weight: 700;
  }
  h1 { font-size: clamp(2rem, 4vw, 3rem); }
  h2 { font-size: clamp(1.5rem, 3vw, 2rem); }
  h3 { font-size: 1.25rem; }
  h4 { font-size: 1rem; text-transform: uppercase; letter-spacing: 0.08em; color: var(--brand-text); }

  p { margin: 0 0 var(--s-3); }
  a { color: var(--brand-primary); text-decoration: underline; text-underline-offset: 3px; }
  a:hover { color: var(--brand-accent); }

  .eyebrow {
    font-family: var(--font-display);
    text-transform: uppercase;
    letter-spacing: 0.12em;
    font-size: 0.75rem;
    color: var(--brand-accent);
    font-weight: 500;
  }

  .card {
    background: var(--brand-white);
    border: 1px solid var(--brand-rule);
    border-radius: var(--radius-md);
    padding: var(--s-4);
    box-shadow: var(--shadow-card);
  }

  .card--tan { background: var(--brand-bg-2); }

  .pill {
    display: inline-block;
    padding: 2px 10px;
    border-radius: 999px;
    font-size: 0.75rem;
    background: var(--brand-bg-2);
    color: var(--brand-primary);
    font-weight: 500;
  }
  .pill--accent { background: var(--brand-accent); color: var(--brand-primary); }

  .btn {
    display: inline-block;
    padding: 10px 18px;
    background: var(--brand-primary);
    color: var(--brand-white);
    border-radius: var(--radius-sm);
    border: 0;
    font-family: var(--font-display);
    font-weight: 500;
    cursor: pointer;
    text-decoration: none;
  }
  .btn:hover { background: var(--brand-accent); color: var(--brand-primary); }

  .container { max-width: 1100px; margin: 0 auto; padding: var(--s-6) var(--s-4); }

  hr { border: 0; border-top: 1px solid var(--brand-rule); margin: var(--s-5) 0; }

  blockquote {
    border-left: 3px solid var(--brand-accent);
    padding: var(--s-2) var(--s-4);
    margin: var(--s-4) 0;
    font-family: var(--font-display);
    font-size: 1.25rem;
    color: var(--brand-primary);
  }

  table { border-collapse: collapse; width: 100%; }
  th, td { text-align: left; padding: var(--s-3); border-bottom: 1px solid var(--brand-rule); }
  th { font-family: var(--font-display); color: var(--brand-primary); font-weight: 500; }

  /* Print */
  @media print {
    body { background: white; }
    .no-print { display: none !important; }
    .card { box-shadow: none; border: 1px solid #ccc; }
    a { color: inherit; }
  }
</style>
```

## Usage ratio
- ~60% forest green / off-white (chrome + text)
- ~30% warm tan (card surfaces, secondary backgrounds)
- ~10% amber (CTAs, highlights, pull quotes, hover states only)

## Accessibility rules
- Forest green on off-white: ~11:1 — passes AA/AAA.
- Amber on off-white: ~3:1 — large text and UI only, never body copy.
- Body text always uses Slate `#4A5568` or Forest Green.

## Banned brand words (avoid in headings / body copy)
revolutionary, game-changing, unlock, leverage, curated, seamless, innovative, exciting, thought leadership, synergy, delve, robust, comprehensive, paradigm, disruptive, world-class, incredible, amazing, best practices, learnings, insights (as a noun).

Preferred swaps: insights → "what I found"; leverage → "use"; learnings → "what I learned"; framework → "structure"; curated → describe the actual selection.
