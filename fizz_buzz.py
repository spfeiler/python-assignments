number = int(input('Enter Number'))

def fizz_buzz(a):
    if a % 3 == 0:
        print('Fizz')
    if a % 5 == 0:
        print('Buzz')
    if a % 3 == 0 and a % 5 == 0:
        print('Fizz Buzz')

fizz_buzz(number)
