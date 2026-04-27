# HPC Code Constraints

If reading or transforming European XFEL data, use the `extra-data` library.

Write the minimum code needed to solve the requested task:

- Do not add features beyond the request.
- Do not add single-use abstractions.
- Do not add configurability unless requested.
- Do not add error handling for impossible scenarios.
- Simplify aggressively when a shorter solution is clearly sufficient.

When editing existing code:

- Do not improve adjacent unrelated code.
- Do not refactor unrelated areas.
- Match existing style.
- If unrelated dead code is found, mention it but do not remove it.
- Remove only orphaned imports, variables, and functions created by your own changes.
- Ensure every changed line is traceable to the user request.
