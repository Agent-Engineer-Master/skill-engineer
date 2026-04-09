# Fix From Logs

> Diagnose bugs from raw error logs, stack traces, or CI output — triages errors, identifies root cause to file/function/line, then proposes a targeted fix and regression test for human approval

**Target user:** Developers and Claude Code operators debugging failing builds, CI pipelines, or production errors

## Install

```bash
cp SKILL.md ~/.claude/skills/
```

Reload Claude Code. Trigger phrase: `here are the logs fix it / diagnose this error / CI is failing here are the logs`

## Example

**Input:**
```
TypeError: Cannot read properties of undefined (reading 'map')
  at ProductList (/app/components/ProductList.jsx:34:12)
  at renderWithHooks (/node_modules/react-dom/cjs/react-dom.development.js:14985:18)

The above error occurred in the <ProductList> component

```

**Output:**
```
Root cause: products prop is undefined on mount — no null guard
Location: ProductList.jsx:34
Fix: products?.map(...) or add if (!products) return null above the map
Confidence: High

Test plan: test_productlist_renders_empty_when_products_undefined (mock the prop as undefined)

```

## Limitations

Works best with source-mapped stack traces. Obfuscated/minified output reduces confidence. Does not handle multi-service distributed traces — works on single-service logs.

---

*Built by [Agent Engineer Master](https://agentengineermaster.com) — production-ready Claude Code skills on demand.*
*Every skill is engineered to the AEM production bar: trigger logic, methodology, output contract, and edge case handling. All four. Every time.*
