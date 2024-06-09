def even_or_odd(n):
    return n%2==0

number=int(input("Enter your number:"))
if even_or_odd(number):
    print('the number is even',number)
else :
    print('the number is odd',number)

