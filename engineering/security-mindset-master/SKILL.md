---
name: security-mindset-master
description: Activate when implementing or modifying API endpoints, authentication or authorization logic, database queries or ORM calls, user input handling, session/token management, file uploads, webhooks, or any feature that stores or transmits user data — gates implementation with threat surface analysis, secure defaults verification, attacker's eye pass, and structural control check before any code ships; do NOT activate for read-only documentation, configuration review, or infrastructure changes unrelated to user data flow
---

# Security Mindset Master

## Overview

Security is a design constraint. Not a checklist. Not a phase. Not someone else's job.

**Core principle:** Think like an attacker during implementation. Reasoning about threats after the code is written is too late — you've already chosen the unsafe path.

**Violating the letter of this rule is violating the spirit of this rule.**

## The Iron Law

```
NO ENDPOINT, DATA ACCESS PATTERN, OR USER INPUT HANDLER SHIPS WITHOUT A SECURITY ANALYSIS FIRST
```

The insecure path must never be the path of least resistance.

## When to Use

**Always — before writing code that touches:**
- API endpoints (new or modified)
- Authentication or authorization logic
- Database queries or ORM calls
- User input of any kind
- Session tokens, JWTs, API keys
- File uploads or downloads
- Webhooks or callbacks
- Any feature that stores or transmits user data

**Not for:**
- Read-only documentation changes
- Infrastructure config unrelated to data flow
- Dependency version bumps with no logic changes

Thinking "this is a small change, security analysis is overkill"? That's rationalization. Small changes to auth logic have caused the largest breaches.

## Phase 1: Threat Surface Analysis

**Complete before writing any code.**

Answer these questions explicitly — not in your head, in the response:

1. **Who can call this?** — authenticated users only? anonymous? other services? what roles or permissions?
2. **What data does it touch?** — classify sensitivity: PII, credentials, financial, internal-only, public
3. **What trust boundaries does it cross?** — user → server, server → DB, server → external API, internal → internal
4. **Worst-case malicious caller** — if an attacker controls this input, what's the most damaging thing they could make the system do?
5. **What if inputs are malformed?** — empty, null, max-length exceeded, unexpected type, Unicode edge cases
6. **What if a request is replayed?** — is the same request sent twice dangerous? is there idempotency protection?
7. **What if the caller substitutes another user's identifier?** — can they access or modify another user's data?

Minimum acceptable output: at least one named threat and its mitigation documented. "No threats identified" is not an acceptable output for any code path touching user data.

## Phase 2: Secure Defaults Checklist

Read `references/secure-defaults.md`. Each gate must be **verified present** — not assumed.

These are non-negotiable. There are no exceptions, only tradeoffs that must be explicitly documented:

- [ ] **Parameterized queries** — no string-concatenated SQL, LDAP, or OS commands anywhere in this code path
- [ ] **Secrets in environment variables** — no credentials, tokens, or keys in source code, comments, or log statements
- [ ] **Auth check explicit in this handler** — not inherited, not assumed from middleware — verify it is present in the code being written
- [ ] **Input validated server-side** — regardless of what client-side validation exists
- [ ] **Sensitive data absent from logs** — no passwords, tokens, PII, or session identifiers in any log call site this code touches
- [ ] **HTTPS enforced, CSRF tokens present** — on all state-changing endpoints
- [ ] **CORS policy explicit and minimal** — no wildcard origins on authenticated endpoints

## Phase 3: Attacker's Eye Pass

Read `references/attacker-patterns.md`. Before writing any code, reason through each attack class for this specific feature:

| Attack | Question to answer |
|--------|--------------------|
| **IDOR** | Can a user modify an ID parameter to access another user's object? Is there a per-object ownership check? |
| **Privilege escalation** | Can a lower-privilege user reach this through a different code path? Is the role check on the resource, not just the route? |
| **Replay attack** | Is a valid request replayable? Are tokens/nonces single-use? |
| **Timing attack** | Does a timing difference between success and failure leak information (e.g., valid vs invalid username)? |
| **Mass assignment** | Does this endpoint bind request parameters to a model? Are bindable fields explicitly allowlisted? |
| **Insecure deserialization** | Does this code deserialize user-supplied data? Is the deserialization format safe? |
| **Error leakage** | Do error responses reveal stack traces, internal paths, DB structure, or version strings? |

Not every attack applies to every feature. Document which you considered, which apply, and how each applicable one is mitigated.

## Phase 4: Structural vs Behavioral Check

**After writing code, before marking done.**

For every security control implemented, ask:

> "If every future developer who touches this code ignores all comments, all docs, and all institutional memory — does this control still hold?"

**Structural** — the unsafe action is syntactically or architecturally impossible: parameterized queries, framework-level CSRF middleware, DB constraints, type system enforcement. **Prefer these.**

**Behavioral** — the control works only if developers remember to use it: a function that must be called manually, a comment saying "always check auth here." **These accrue debt.**

If a control is behavioral: either redesign it to be structural, or document the explicit risk acceptance with the reason redesign isn't feasible.

## Red Flags — Stop Execution

These patterns require an **immediate stop**. Do not work around them. Fix them or escalate.

| Pattern | Stop Reason |
|---------|-------------|
| String concatenation in any query | SQL / LDAP / command injection. Parameterize it. |
| `password`, `secret`, `token`, or `key` in a log statement | Credentials in logs. Remove unconditionally. |
| Endpoint handler with no visible auth/session check | Unauthenticated access. Add the check before continuing. |
| `CORS: *` or equivalent wildcard on an authenticated endpoint | Cross-origin credential theft. Specify allowed origins explicitly. |
| User-supplied data in a file path or shell command | Path traversal or command injection. Restrict and sanitize. |
| Error response includes stack trace or internal state | Information leakage. Return generic errors; log detail server-side. |
| "I'll add auth after the feature works" | This is how auth never gets added. Add it now. |

## Common Rationalizations

| Rationalization | Reality |
|----------------|---------|
| "It's an internal endpoint" | Internal endpoints get compromised. Supply chain attacks, SSRF, and misconfigured VPCs hit internal services routinely. Defense in depth means internal = untrusted. |
| "The client validates it" | Clients can be bypassed. Any attacker posts directly to the API. Server-side validation is non-negotiable regardless of frontend logic. |
| "We're behind a VPN / firewall" | Perimeter security fails. Assume breach. Zero-trust is the baseline, not the advanced model. |
| "It's just test data" | Test environments get used with real credentials. They share code paths with production. Treat them identically. |
| "I'll harden it before launch" | Security bolted on after is weaker, slower to ship, and requires revisiting every data access path. The debt compounds. |
| "Automated scanners would catch it" | IDOR, business logic flaws, and timing attacks are routinely missed by scanners. They find known patterns. You are writing the unknown pattern. |
| "UUIDs prevent IDOR" | Non-guessable IDs are defense-in-depth, not access control. If an ID leaks through any related endpoint, the vulnerability is exploitable. Per-object ownership checks are required regardless. |

## Verification Checklist

Run after code is written, before marking the task complete. See also `superpowers:verification-before-completion`.

- [ ] Completed Phase 1 threat surface analysis before writing any code
- [ ] Documented at least one named threat and its mitigation — "no threats found" is not acceptable
- [ ] All Phase 2 secure defaults present and verified by reading the code — not assumed
- [ ] Completed Phase 3 attacker's eye pass — documented which attack classes apply and how each is mitigated
- [ ] Phase 4 check done — security controls are structural where possible; behavioral controls have explicit risk documentation
- [ ] No sensitive data in logs — verified by reading every log call site in the code written
- [ ] Auth check is explicit in this handler — not inherited from hope, verified present in the code

---
<!-- Built with Agent Engineer Master — get your own production-ready skill: www.agentengineermaster.com/skill-engineer -->
