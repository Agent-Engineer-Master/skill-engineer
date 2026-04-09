# Test Writing Rules (Python / pytest)

## Table of Contents
1. [Test File Conventions](#1-test-file-conventions)
2. [Function Signature Template](#2-function-signature-template)
3. [Naming Rules](#3-naming-rules)
4. [Mocking Rules](#4-mocking-rules)
5. [Assertion Rules](#5-assertion-rules)
6. [Failing-First Discipline](#6-failing-first-discipline)
7. [Anti-Patterns to Avoid](#7-anti-patterns-to-avoid)
8. [CI Integration Checklist](#8-ci-integration-checklist)

---

## 1. Test File Conventions

- Test file location: `tests/test_<module_name>.py` — mirror the module path
- If `tests/` does not exist: create it with an empty `__init__.py`
- One test file per production module; do not mix concerns
- Import the module under test with an absolute import — never `sys.path` hacks
- Required imports for every regression test file:

```python
from unittest.mock import MagicMock, patch, call
import pytest
```

---

## 2. Function Signature Template

All test functions must be typed:

```python
def test_<scenario_description>(mock_<dependency>: MagicMock) -> None:
```

Example:

```python
def test_checkout_raises_value_error_when_payment_gateway_returns_none(
    mock_payment_gateway: MagicMock,
) -> None:
```

For fixtures:

```python
@pytest.fixture
def mock_db_session() -> MagicMock:
    session = MagicMock()
    session.query.return_value.filter.return_value.first.return_value = None
    return session
```

---

## 3. Naming Rules

**Format:** `test_<subject>_<condition>_<expected_outcome>`

| Component | Rule |
|---|---|
| `subject` | The function or method under test |
| `condition` | The specific input state or external condition that triggers the bug |
| `expected_outcome` | What the code should do (raise, return, call, not call) |

**Good names:**
- `test_process_order_raises_when_inventory_service_returns_none`
- `test_send_email_does_not_call_smtp_when_recipient_list_is_empty`
- `test_parse_config_returns_default_port_when_env_var_missing`

**Bad names (reject these):**
- `test_edge_case`
- `test_bug_fix_123`
- `test_process_order_2`

**Required comment in every regression test:**

```python
# Regression: [one-sentence root cause statement]
# Log evidence: [paste the relevant log line]
```

---

## 4. Mocking Rules

**Always mock at the boundary of the unit under test** — not deep inside dependencies.

**Standard patterns:**

```python
# Mock a method on an object
with patch.object(MyClass, "method_name", return_value=None) as mock_method:
    ...

# Mock an entire module-level import
with patch("mymodule.requests.get") as mock_get:
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"key": "value"}
    ...

# Mock using pytest-mock (if available)
def test_foo(mocker: pytest.MonkeyPatch) -> None:
    mock_fn = mocker.patch("mymodule.some_function", return_value=42)
    ...
```

**What to mock:**
- HTTP calls (requests, httpx, aiohttp)
- Database sessions / ORM calls
- File system reads/writes (use `tmp_path` fixture for file tests)
- External service clients (Stripe, Shopify, SendGrid)
- `datetime.now()` / `time.time()` — use `freezegun`
- `os.environ` — use `monkeypatch.setenv`
- Random number generators — `random.seed(42)` before the call

**What NOT to mock:**
- The module under test itself
- Pure functions with no side effects
- Simple data classes or value objects

**Set explicit return values — never rely on MagicMock's default auto-spec:**

```python
# Bad: relies on MagicMock auto-return (always truthy, hides None bugs)
mock_service = MagicMock()

# Good: explicit
mock_service.get_user.return_value = None  # or a real User fixture
```

---

## 5. Assertion Rules

**Assert the specific violated state, not just "no exception":**

```python
# Bad — passes even if the bug returns wrong data silently
result = process_order(order)
assert result is not None

# Good — asserts the exact contract violated by the bug
with pytest.raises(ValueError, match="payment gateway returned None"):
    process_order(order)

# Good — asserts the specific return value
result = parse_config(env={})
assert result.port == 8080  # default port when env var missing

# Good — asserts a mock was called (or not called) with specific args
mock_smtp.send.assert_not_called()
mock_logger.error.assert_called_once_with("Payment gateway unavailable")
```

**When the bug is a silent wrong value** (no exception raised):

```python
assert result == expected_value, (
    f"Expected {expected_value!r}, got {result!r}. "
    "This is a regression for: [root cause statement]"
)
```

---

## 6. Failing-First Discipline

Before writing the fix:

1. Run the test: `pytest tests/test_module.py::test_function_name -v`
2. Confirm it **fails**
3. Confirm the failure message matches the bug (not a wrong assertion or import error)
4. Only then write the fix

If the test passes on the first run: the root cause is wrong. Do not proceed. Return to Phase 2 of the skill.

**Failure messages that indicate a wrong test (not a real fail):**
- `ImportError` or `ModuleNotFoundError` — fix the import, not the production code
- `AttributeError` on the mock itself — mock is misconfigured
- `PASSED` — root cause misidentified; revisit Phase 2

---

## 7. Anti-Patterns to Avoid

| Anti-Pattern | Why | Instead |
|---|---|---|
| `assert True` or empty test body | Proves nothing | Assert the exact violated state |
| Catching and suppressing exceptions in the test | Hides failures | Let exceptions propagate; use `pytest.raises` |
| Testing implementation details (private methods, internal state) | Brittle — breaks on refactor | Test observable behaviour (return values, side effects) |
| Mocking the return value to the "correct" value before testing | The test will always pass | Set the mock to return what the bug returns (e.g., `None`) |
| Multiple unrelated assertions in one test | Hard to diagnose which assertion caught the regression | One behaviour per test |
| `time.sleep()` in tests | Flaky and slow | Mock time with `freezegun` |
| Writing test after the fix | Defeats the purpose — you can't confirm the test caught the bug | Always write test first |

---

## 8. CI Integration Checklist

Before declaring the fix complete:

- [ ] New test file is in `tests/` and follows naming convention
- [ ] `pytest tests/test_<module>.py::test_<name> -v` passes (green)
- [ ] `pytest` (full suite) passes with no new failures
- [ ] Test has the regression comment with root cause + log evidence
- [ ] No `print()` statements left in test or production code
- [ ] If a new dependency was needed (`freezegun`, `pytest-mock`): it is added to `requirements.txt` or `pyproject.toml`
