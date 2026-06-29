"""Luhn's Algorithm - Card/Aadhar Number Validation

Implements the Luhn algorithm to validate credit card and Aadhar numbers.
"""

def verification(card_no):
    """Verify if a card/Aadhar number is valid using Luhn's algorithm.
    
    Args:
        card_no (str): The card number to validate
    
    Returns:
        bool: True if valid, False otherwise
    """
    try:
        # Ensure only digits
        if not card_no.isdigit():
            return False
        
        # Reverse the number
        card_no_reverse = card_no[::-1]
        
        # Sum odd position digits (1st, 3rd, 5th...)
        sum_odd = 0
        odd = card_no_reverse[::2]
        for i in odd:
            sum_odd += int(i)
        
        # Sum even position digits (2nd, 4th, 6th...)
        sum_even = 0
        even = card_no_reverse[1::2]
        for i in even:
            no = int(i) * 2
            # If result is 2 digits, add them together
            if no >= 10:
                no = (no // 10) + (no % 10)
            sum_even += no
        
        total = sum_odd + sum_even
        return total % 10 == 0
    
    except (ValueError, AttributeError):
        return False

def main():
    """Main function to run the card validation program."""
    print("="*50)
    print("   CARD/AADHAR NUMBER VALIDATOR")
    print("="*50)
    
    while True:
        card_no = input('\nEnter your card/Aadhar number (or "exit" to quit): ').strip()
        
        if card_no.lower() == 'exit':
            print("\nThank you! Goodbye!")
            break
        
        # Remove spaces and dashes
        modified = str.maketrans({'-': '', ' ': ''})
        translated = card_no.translate(modified)
        
        if verification(translated):
            print(f"✓ Valid number: {translated}")
        else:
            print(f"✗ Invalid number: {translated}")

if __name__ == "__main__":
    main()
