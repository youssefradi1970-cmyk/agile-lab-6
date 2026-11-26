# Task C1: Smells in legacy_invoice.py

| Smell | Where | Principle it breaks |
|---|---|---|
| Long if/elif chain on `kind` | loop body and after the loop | OCP: a new student type means editing this function |
| Magic numbers (1200, 0.5, 2000, 5000) | inside the if/elif chain | Readability: no names explain the numbers |
| One function calculates, formats text, writes a file and prints | whole `make_invoice` | SRP: more than one reason to change |
| File opened without `with` and written directly to disk | `open(...)` and `f.close()` | DIP: depends on the disk, cannot be tested without writing files |
| Fee worked out per course although only total hours matter | the `for` loop | Unnecessary complexity |