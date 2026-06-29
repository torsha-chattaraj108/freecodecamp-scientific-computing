def case_converter(pascal_or_camel_cased):
    snake_cased_char=[]
    for char in pascal_or_camel_cased:
        if char.isupper():
            converted='_'+char.lower()
            snake_cased_char.append(converted)
        else:
            snake_cased_char.append(char)
    snake_cased_string=''.join(snake_cased_char)
    clean_snake_cased_string=snake_cased_string.strip('_')
    return clean_snake_cased_string

def main():
    print(case_converter('aLongAnComplexSrting'))

main()
