"""Snake Case Converter - Method 2

Convert PascalCase or camelCase strings to snake_case using list comprehension.
"""

def convert_case(pascal_or_camel_cased_string):
    """Convert PascalCase or camelCase to snake_case using list comprehension.
    
    Args:
        pascal_or_camel_cased_string (str): String in PascalCase or camelCase
    
    Returns:
        str: String converted to snake_case
    
    Example:
        >>> convert_case('IAmAPascalCasedString')
        'i_am_a_pascal_cased_string'
    """
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper() else char 
        for char in pascal_or_camel_cased_string
    ]
    return ''.join(snake_cased_char_list).strip('_')

def main():
    """Test the case converter."""
    print("="*50)
    print("   SNAKE CASE CONVERTER - METHOD 2 (List Comprehension)")
    print("="*50)
    
    test_cases = [
        'IAmAPascalCasedString',
        'myVariableName',
        'DataParser',
        'parseJSONResponse',
        'getXMLData'
    ]
    
    for test in test_cases:
        result = convert_case(test)
        print(f"{test:30} -> {result}")

if __name__ == "__main__":
    main()
