def verification(card_no):
    sum_odd=0
    card_no_reverse=card_no[::-1]
    odd=card_no_reverse[::2]
    for i in odd:
        sum_odd+=int(i)
    sum_even=0
    even=card_no_reverse[1::2]
    for i in even:
        no=int(i)*2
        if no>=10:
            no=(no//10)+(no%10)
        sum_even+=no
    total=sum_odd+sum_even
    return total%10==0

def main():
    card_no=input('enter your aadhar number here to check if valid or not: ')
    modified=str.maketrans({'-':'',' ':''})
    translated=card_no.translate(modified)
    if verification(translated):
        print('valid')
    else:
        print('invalid')

main()
