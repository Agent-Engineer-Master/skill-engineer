# Attacker Patterns Reference

Attack mechanics, detection questions, and fixes for Phase 3 of `security-mindset-master`.

For each attack class: document whether it applies to the current feature, and if so, how it is mitigated.

---

## IDOR — Insecure Direct Object Reference

**Mechanism:** An endpoint accepts a user-controlled identifier and uses it to retrieve or modify a resource without verifying the caller owns or has rights to that specific object.

**Attack scenario:**
```
GET /api/invoices/1042   → attacker's invoice (valid)
GET /api/invoices/1043   → victim's invoice (attacker changes one digit)
```

**Detection questions:**
- Does this endpoint accept any identifier in the URL, query string, or body?
- Is there a per-object ownership or role check — not just route-level auth?
- Can an authenticated user enumerate IDs they don't own?

**Fix:**
```python
obj = Resource.query.get_or_404(resource_id)
if obj.owner_id != current_user.id:
    abort(403)
```

**Common mistake:** Using UUIDs and calling it fixed. Non-guessable ≠ access-controlled. If a UUID leaks through any related endpoint, the vulnerability is exploitable. Ownership checks are required regardless of ID format.

---

## Privilege Escalation

**Mechanism:** A lower-privilege user reaches a higher-privilege action through an alternative code path — a missing role check on a sub-resource, a parameter that overrides role, or a direct object call that bypasses the middleware guard.

**Detection questions:**
- Is the role/permission check on the resource itself, or only on the route?
- Can a user with role A reach this feature via an endpoint designed for role B?
- Does this endpoint accept `role`, `admin`, `is_staff`, `subscription_tier`, or similar fields from the request body?
- Can a user escalate by modifying their own profile through a different endpoint?

**Common scenario:** `/admin/users` is guarded, but `/api/users/{id}/promote` is not — and both set `user.role = 'admin'`.

**Fix:** Role check on the action, not just the route. Treat `role` and `admin` as read-only fields from the server's perspective — never bind them from request input.

---

## Replay Attack

**Mechanism:** A valid request captured in transit or from logs is submitted again. If the server cannot distinguish the replay from a fresh request, the action executes twice.

**When it matters:** Payment actions, password reset links, one-time codes, webhook deliveries, OAuth flows, idempotency-sensitive operations.

**Detection questions:**
- Is this action idempotent by design (safe to replay)?
- If not: is there a nonce, timestamp, or sequence number that makes each request unique?
- Are one-time tokens invalidated immediately upon first use?
- Do webhook signatures include a timestamp, and is replay within a time window rejected?

**Fix:** Include a short-lived nonce in the token or request signature. Validate on receipt and invalidate on use. For webhooks: verify timestamp is within an acceptable window (e.g., ±5 minutes) before processing.

---

## Timing Attack

**Mechanism:** The time taken to process a request leaks information about internal state. A login endpoint that short-circuits on unknown usernames responds faster than one that computes a hash comparison for a valid username with a wrong password — revealing which usernames are valid.

**When it matters:** Login flows, password comparison, token comparison, account existence checks, any branch where "close to valid" takes longer than "completely wrong."

**Detection questions:**
- Does this code path return faster for some invalid inputs than others?
- Are sensitive string comparisons done with `==` instead of a constant-time function?
- Does the error message distinguish between "user not found" and "wrong password"?

**Fix:**
```python
# Python — constant-time comparison
import hmac
if not hmac.compare_digest(provided_token.encode(), stored_token.encode()):
    return unauthorized()
```
```javascript
// Node — constant-time comparison
const crypto = require('crypto');
if (!crypto.timingSafeEqual(Buffer.from(provided), Buffer.from(stored))) {
    return res.status(401).json({ error: "Invalid credentials" });
}
```

Return the same error message for "user not found" and "wrong password." Complete the full comparison before returning regardless of branch.

---

## Mass Assignment

**Mechanism:** A framework auto-binds request parameters to model fields. An attacker submits fields the developer didn't intend to expose — `role`, `admin`, `balance`, `subscription_tier`.

**Attack scenario:**
```json
POST /api/users/profile
{"name": "Alice", "email": "alice@example.com", "role": "admin"}
```

**Detection questions:**
- Does this endpoint bind request data to an ORM model automatically?
- Is there an explicit allowlist of fields that may be set from this endpoint?
- Can a user set any privileged fields by including them in the request body?

**Fix:**
```python
# Bad — binds everything
user.update_from_dict(request.json)

# Good — explicit allowlist
ALLOWED_PROFILE_FIELDS = {'name', 'email', 'bio', 'timezone'}
safe_data = {k: v for k, v in request.json.items() if k in ALLOWED_PROFILE_FIELDS}
user.update_from_dict(safe_data)
```

In Rails: `params.permit(:name, :email, :bio)`. In Laravel: `$request->only(['name', 'email'])`. In Spring: `@JsonIgnoreProperties` or explicit `@RequestBody` DTO with only the intended fields.

---

## Insecure Deserialization

**Mechanism:** Deserializing user-supplied data using formats that support arbitrary object instantiation or code execution.

**Unsafe formats for user-supplied data:**
- Python `pickle` / `shelve`
- Java native serialization (`ObjectInputStream`)
- PHP `unserialize()`
- Ruby `Marshal.load`
- YAML with class instantiation (`!!python/object`, `!!ruby/object`)

**Safe formats for user-supplied data:** JSON (no `eval`), Protobuf, MessagePack with schema validation, CBOR with schema.

**Detection questions:**
- Does this code deserialize any user-supplied bytes or strings?
- Is the deserialization format on the unsafe list above?
- If a legacy unsafe format is required: is there an HMAC signature verified before deserialization?

**Fix:** Use JSON or schema-validated binary formats for user data. If legacy format is unavoidable: sign with HMAC, verify signature before deserializing, deserialize in a sandboxed subprocess.

---

## Error Leakage

**Mechanism:** Error responses reveal implementation details — stack traces, file paths, database structure, table names, server versions, or branch behavior that distinguishes valid from invalid inputs.

**What attackers extract:**
- Stack traces → internal file paths, class names, framework version, dependency versions
- Database errors → schema structure, table names, column names, query patterns
- "Invalid username" vs "Invalid password" → valid username enumeration
- Server headers → framework and version for targeted CVE exploitation

**Detection questions:**
- Do error responses in this code path include exception messages or stack traces?
- Does the error distinguish between "entity not found" and "not authorized to access it"?
- Are server version headers (`X-Powered-By`, `Server`) stripped or suppressed?
- Are database errors caught before they propagate to the response?

**Fix:**
```python
# Bad — leaks internals
except Exception as e:
    return {"error": str(e), "traceback": traceback.format_exc()}, 500

# Good — log internally, return generic externally
except Exception as e:
    logger.error(f"Unhandled exception in {request.endpoint}", exc_info=True)
    return {"error": "An internal error occurred. Please try again."}, 500
```

For "not found" vs "not authorized": return 404 for both when the distinction leaks object existence to the caller.

---

## Structural vs Behavioral Controls — Decision Guide

Before implementing any security control, classify it:

| Control | Behavioral (avoid) | Structural (prefer) |
|---------|-------------------|---------------------|
| SQL injection prevention | Policy: "always parameterize" | ORM enforces parameterization; no raw escape hatch |
| Missing auth check | Code review + documentation | Framework opt-out model: everything requires auth unless decorated `@public` |
| Mass assignment | Developer remembers to allowlist | Explicit DTO / `permit()` enforced at framework level; no auto-bind |
| Secret leakage | Policy: "don't commit secrets" | Pre-commit hook + CI scan blocks push |
| IDOR | Code review | Auth library that enforces ownership at the query layer |
| CSRF | Developer includes token | Framework middleware applied globally; opt-out required, not opt-in |

**When structural is not feasible:** Document the behavioral control explicitly, add an automated test that proves the control works under adversarial input, and flag the pattern for architectural review at the next refactor.
