# Secure Defaults Reference

Detailed pass/fail criteria for Phase 2 of `security-mindset-master`.

---

## 1. Parameterized Queries

**Gate:** No string-concatenated SQL, LDAP, or OS commands anywhere in this code path.

**Pass:**
```python
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
```
```javascript
db.query("SELECT * FROM users WHERE id = ?", [userId])
```
```ruby
User.where(id: user_id)
```

**Fail:**
```python
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
cursor.execute("SELECT * FROM users WHERE id = " + user_id)
```

**Special cases that bypass ORM protection:**
- `whereRaw()`, `raw()`, `execute()` with interpolation — treat as raw SQL, apply same rules
- Dynamic `ORDER BY` clauses cannot be parameterized — use an allowlist of valid column names
- Table and column names cannot be parameterized — allowlist or reject

---

## 2. Secrets in Environment Variables

**Gate:** No credentials, tokens, or keys in source code, comments, or log statements.

**Pass:**
```python
api_key = os.environ["STRIPE_API_KEY"]
db_password = os.getenv("DB_PASSWORD")
```

**Fail:**
```python
api_key = "sk_live_abc123"
db_password = "hunter2"  # TODO: move this to env
```

**Checklist:**
- `.env` files are in `.gitignore` — verified, not assumed
- No keys in test fixtures, seed files, or example configs committed to version control
- Secret manager (Vault, AWS Secrets Manager, GCP Secret Manager) used for production secrets
- Rotation is possible — hardcoded secrets cannot be rotated without a deploy

---

## 3. Auth Check Explicit in Handler

**Gate:** Authentication and authorization are explicitly present in the code being written — not assumed from middleware or inherited from a calling function.

**Pass — both auth and per-object authorization:**
```python
@app.route("/api/documents/<doc_id>")
@login_required
def get_document(doc_id):
    doc = Document.query.get_or_404(doc_id)
    if doc.owner_id != current_user.id:
        abort(403)
    return jsonify(doc)
```

**Fail — auth assumed, authorization missing:**
```python
@app.route("/api/documents/<doc_id>")
def get_document(doc_id):
    # assumes middleware handles auth — verify this is actually true
    doc = Document.query.get_or_404(doc_id)
    return jsonify(doc)  # no ownership check
```

**Key distinction:** Authentication ("is this user logged in?") ≠ Authorization ("does this user own this object?"). Both must be present. Route-level guards do not substitute for per-object ownership checks.

---

## 4. Server-Side Input Validation

**Gate:** Input is validated server-side regardless of client-side validation.

**Allowlist over blocklist — define what valid looks like, reject everything else:**

```python
# Bad — blocklist misses encodings, Unicode, and context-specific payloads
if "<script>" in user_input:
    reject()

# Good — allowlist
import re
if not re.match(r'^[a-zA-Z0-9_\-]{1,64}$', username):
    return {"error": "Invalid username format"}, 400
```

**Checklist:**
- [ ] Type: is the input the expected type?
- [ ] Length: minimum and maximum length checked?
- [ ] Format: regex, enum, or schema validation applied?
- [ ] Range: numeric inputs bounded?
- [ ] Null/empty handled explicitly — not assumed safe

**File uploads specifically:**
- Validate by file content (magic bytes) — not filename extension
- Restrict MIME types to an explicit allowlist
- Set maximum file size server-side
- Store uploads outside the web root
- Generate new filenames server-side — never use user-supplied filenames in storage paths

---

## 5. Sensitive Data Absent from Logs

**Gate:** No passwords, tokens, PII, or session identifiers appear in any log call site this code touches.

**Fail patterns:**
```python
logger.info(f"Login attempt: {username} / {password}")
logger.debug(f"Request headers: {request.headers}")   # contains Authorization
logger.error(f"Token validation failed for: {token}")
logger.info(f"User object: {user.__dict__}")           # may contain sensitive fields
```

**Pass — log what happened, not what the secret is:**
```python
logger.info(f"Login attempt for user_id={user_id} result=failed")
logger.error(f"Token validation failed — token_prefix={token[:8]}...")
logger.info(f"Request to {endpoint} from user_id={user_id}")
```

**Review procedure:** Read every log call site in the code path being modified. Do not assume logs are clean.

---

## 6. HTTPS + CSRF

**Gate:** HTTPS enforced for all endpoints. CSRF tokens present on all state-changing endpoints.

**HTTPS:**
- Redirect HTTP → HTTPS at load balancer or application level
- HSTS header: `Strict-Transport-Security: max-age=31536000; includeSubDomains`
- `Secure` flag on all cookies

**CSRF:**
- State-changing endpoints (POST, PUT, PATCH, DELETE) require a CSRF token
- Token must be verified server-side — presence in the form is not sufficient
- API endpoints using Authorization header (not cookies) for auth are exempt if cookies play no auth role
- `SameSite=Strict` or `SameSite=Lax` on session cookies provides defense-in-depth

---

## 7. CORS Policy

**Gate:** CORS policy is explicit and minimal. No wildcard origins on authenticated endpoints.

**Pass:**
```
Access-Control-Allow-Origin: https://app.yourdomain.com
Access-Control-Allow-Credentials: true
```

**Fail:**
```
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
```

**Rules:**
- `*` is acceptable only on fully public, unauthenticated, read-only endpoints
- Allowed origins must be an explicit list — not derived from the request's `Origin` header
- Pre-flight OPTIONS requests must return the same restrictive policy
- Do not rely on browser enforcement of the `*` + credentials incompatibility — reject at the server
