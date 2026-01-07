## Bug 001 – Division by Zero

**Problem:**  
Calling `average()` with an empty list causes a `ZeroDivisionError`.

**Root cause:**  
No guard condition for empty input.

**Fix:**  
Added input validation to handle empty lists safely.

**Outcome:**  
Function now fails gracefully instead of crashing.
