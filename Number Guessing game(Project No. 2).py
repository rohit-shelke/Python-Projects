from random import *
x = randint(0,100)
c = 0
while True:
    a = int(input('Enter the number:'))
    if a==x:
        print('You guessed it right!!! You won!!!')
        break
    if a>x:
        print('Your entered number is greater than the number')
    elif a<x:
        print('Your entered number is smaller than the number')
    c = c + 1
print('No. of chances taken =',c )
