import re
import secrets
import string

def generate_password(length=16,num=1,special_chars=1,uppercase=1,lowercase=1):
    #Enter the characters
    letters=string.ascii_letters
    digits=string.digits
    symbols=string.punctuation
    #Combine the characters
    all_characters=letters+digits+symbols
    #Build the password
    while True:
        password=''
        for _ in range(length):
            password+=secrets.choice(all_characters)
        constraints=[
            (num,r'\d'),
            (special_chars,fr'[{symbols}]'),
            (uppercase,r'[a-z]'),
            (lowercase,r'[A-Z]')
            ]
        #Check if the password is strong
        if all(constraint<=len(re.findall(pattern,password))for constraint,pattern in constraints):
            break
    return password

__name__=='__main__'
new_password=generate_password()
print('Generated password: ',new_password)
