# freecodecamp-scientific-computing
Python projects from FCC scientific computing class 11 

# Password Generator

This repository contains Python projects from the FreeCodeCamp scientific computing curriculum. The primary script added here is a secure password generator.

## Files

- `generate_password.py` — A function and script that generates a random password using Python's `secrets` module. The function `generate_password(...)` accepts parameters to require a minimum number of digits, special characters, uppercase and lowercase letters.

## Description

`generate_password.py` uses cryptographically secure randomness (`secrets.choice`) and regular expressions to ensure generated passwords meet the requested minimum counts for different character types. The script prints one generated password when run directly.

## Usage

Run the script directly to print one password with default parameters (length 16):

```bash
python generate_password.py
```

Or import and call the function from another script or an interactive session:

```python
from generate_password import generate_password

pw = generate_password(length=12, num=2, special_chars=2, uppercase=2, lowercase=2)
print(pw)
```

## Notes and recommendations

- The function will loop until a password meeting all constraints is found. If the sum of the minimum counts (digits + special_chars + uppercase + lowercase) exceeds `length`, the loop may run indefinitely or take a very long time. It is recommended to keep the sum less than or equal to `length`.
- Consider adding a validation check in `generate_password` to raise a `ValueError` when the minimum counts exceed the total length.
- Consider adding a small command-line interface (using `argparse`) to allow users to set parameters from the command line.
- Adding unit tests to verify generated passwords consistently meet constraints is recommended.

## Next steps I can help with

- Add a validation check to `generate_password` to prevent infeasible constraints.
- Add a CLI (argparse) so you can pass length and constraint values on the command line.
- Remove the old file with a space in its name (`generate password.py`) so only `generate_password.py` remains.

Tell me which of the above you'd like and I'll apply it.
