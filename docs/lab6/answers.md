# Lab 6 Answers

## Task A1
No. 100% coverage only shows that every line was executed by a test; it does not prove the code is correct, because the tests may still miss wrong results, missing rules, or untested input combinations.


## Task C1
See `smells.md` (5 smells with the principle each one breaks).

## Task C2
`SiblingPolicy` (25% off the regular fee) was added test-first: one class and one entry in `POLICIES`. `make_invoice` was not changed.

## Before / After (make_invoice)

| Measure | Before | After |
|---|---|---|
| Cyclomatic complexity (Ruff C901) | 6 | 1 |
| Tests passing | 3 | 10 |
| Add a new student type | Edit if/elif chains | Add one class + one dict entry |
| Test without writing files | Not possible | Yes, with FakeWriter |