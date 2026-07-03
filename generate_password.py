import re
import secrets
import string


def generate_password(length=16, num=1, special_chars=1, uppercase=1, lowercase=1):
    """Generate a random password satisfying minimum counts for different character types.

    Args:
        length (int): Total password length.
        num (int): Minimum number of digits required.
        special_chars (int): Minimum number of special characters required.
        uppercase (int): Minimum number of uppercase letters required.
        lowercase (int): Minimum number of lowercase letters required.

    Returns:
        str: Generated password.
    """
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    all_characters = letters + digits + symbols

    # Pre-escape symbols for safe regex character class usage
    escaped_symbols = re.escape(symbols)

    while True:
        # Build password using secrets.choice for cryptographic randomness
        password = ''.join(secrets.choice(all_characters) for _ in range(length))

        constraints = [
            (num, r"\d"),
            (special_chars, fr"[{escaped_symbols}]"),
            (uppercase, r"[A-Z]"),
            (lowercase, r"[a-z]")
        ]

        # Check if the password meets all constraints
        if all(count <= len(re.findall(pattern, password)) for count, pattern in constraints):
            break

    return password


if __name__ == '__main__':
    new_password = generate_password()
    print('Generated password:', new_password)
