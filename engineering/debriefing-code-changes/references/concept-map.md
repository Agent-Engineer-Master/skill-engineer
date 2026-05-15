# Concept Map Guardrails

Use named concepts sparingly and only with evidence.

## Common patterns worth naming when visible

- Adapter: a wrapper translates one interface/API shape into another expected by the app.
- Strategy: caller accepts interchangeable implementations behind the same interface and selects among them.
- Dependency injection: dependencies are passed in or configured externally rather than constructed directly inside the unit.
- Repository: data access is isolated behind a persistence-facing abstraction.
- Facade: a simpler API hides multiple lower-level operations.
- Observer/pub-sub: producers emit events that subscribers consume without direct coupling.
- Render prop / function-as-child: React component receives a function that controls part of rendering behavior.
- State machine: explicit states and transitions constrain allowed behavior.

## Evidence standard

For every concept, include:

```
Concept: [name]
Evidence: [file:function or file:line]
Why it fits: [structural reason]
Why it matters here: [tradeoff or learning point]
```

If the evidence is weak, do not name the pattern. Explain the local code shape plainly instead.
