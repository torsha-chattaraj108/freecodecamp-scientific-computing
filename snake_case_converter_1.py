"""Snake Case Converter - Method 1

Convert PascalCase or camelCase strings to snake_case using a loop.
"""

def case_converter(pascal_or_camel_cased):
    """Convert PascalCase or camelCase to snake_case using a loop.
    
    Args:
        pascal_or_camel_cased (str): String in PascalCase or camelCase
    
    Returns:
        str: String converted to snake_case
    
    Example:
        >>> case_converter('aLongAndComplexString')
        'a_long_and_complex_string'
    """
    snake_cased_char = []
    
    for char in pascal_or_camel_cased:
        if char.isupper():
            converted = '_' + char.lower()
            snake_cased_char.append(converted)
        else:
            snake_cased_char.append(char)
    
    snake_cased_string = ''.join(snake_cased_char)
    clean_snake_cased_string = snake_cased_string.strip('_')
    
    return clean_snake_cased_string

def main():
    """Test the case converter."""
    print("="*50)
    print("   SNAKE CASE CONVERTER - METHOD 1 (Loop)")
    print("="*50)
    
    test_cases = [
        'aLongAndComplexString',
        'MyVariableName',
        'URLParser',
        'getHTTPResponseCode',
        'HTTPResponseCodeXML'
    ]
    
    for test in test_cases:
        result = case_converter(test)
        print(f"{test:30} -> {result}")

if __name__ == "__main__":
    main()
