# Decompose Work Into Verifiable Goals

For multi-step tasks, provide a brief plan using verifiable checks:

```bash
1. [Step] > verify: [check]
2. [Step] > verify: [check]
3. [Step] > verify: [check]
```

Prefer testable decomposition patterns such as:

- Reproduce bug with a test, then fix and verify passing.
- Add failing validation tests first, then make them pass.
- Confirm tests pass before and after refactors.
