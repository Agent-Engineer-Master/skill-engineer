# Context Augmentation Guide

How to efficiently pack codebase context for Step 3 — adapted from AutoPrompter findings (+27% edit correctness).

---

## The problem

LLMs degrade significantly beyond 100K tokens of context. Naively dumping an entire codebase into context causes:
- Context rot (earlier files forgotten)
- False relevance (unrelated code influences proposals)
- Slow, expensive inference

This guide gives a targeted scanning protocol to find the right files without the noise.

---

## Scanning order (most signal-efficient first)

### 1. Entry points and routing
Search for the UI label, route name, or feature keyword in routing files first:

```
Glob: **/router.*, **/routes.*, **/App.*, **/index.*
Grep: "[theme keyword]" in those files
```

Routes reveal which component handles the user's journey — read the component, not the whole app.

### 2. Component / module search by keyword
Derive 2-3 search terms from the user intent (not the literal feedback):

| User intent | Search terms |
|------------|-------------|
| "navigate to settings" | `settings`, `SettingsPage`, `preferences` |
| "submit form" | `handleSubmit`, `onSubmit`, `FormSubmit` |
| "load faster" | `useEffect`, `fetch`, `loading`, `skeleton` |

```
Grep: [term1] across **/*.{ts,tsx,js,jsx,py,go,...}
Grep: [term2] across same
```

Read only files with 2+ matches in the same file, or 1 match in a clearly named file.

### 3. Test files
After identifying the component/module, find its test file:

```
Glob: **/{ComponentName}.test.*, **/{ComponentName}.spec.*
```

Read the test file to understand the current behaviour contract before proposing changes.

### 4. Shared utilities and hooks
If the component imports from a shared utility, read that utility too — changes there affect everything that imports it. Flag this as ⚠ Touches shared code in the proposal.

---

## What NOT to read

- `node_modules/`, `vendor/`, `dist/`, `build/`, `.git/`
- Lock files (`package-lock.json`, `yarn.lock`, `go.sum`)
- Generated files (anything with `// Code generated` header)
- Config files unrelated to the theme (`eslint`, `prettier`, `tsconfig` unless the theme is a build/config issue)

---

## Context budget guideline

| Codebase size | Max files to read per theme | Strategy |
|--------------|---------------------------|---------|
| <10K LOC | Up to 10 files | Read freely |
| 10K–100K LOC | Up to 6 files | Routing → component → test only |
| >100K LOC | Up to 4 files | Component + test + 1 shared dep |

If more than 4 files seem essential for a single theme, flag it to the user:
> "This theme touches [N] files. I recommend scoping to [X, Y, Z] for this proposal — do you want broader coverage?"

---

## Fresh context per atomic change

When implementing (Step 5), start each theme's edit with a fresh read of the target file — do not rely on the version read in Step 3. Files may have been modified between steps.
