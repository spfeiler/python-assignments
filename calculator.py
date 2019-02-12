first_number = int(input('Enter First Number'))
operand = input('Enter Operand')
second_number = int(input('Enter Second Number'))

def add(a, b):
    sum = a + b
    if operand == '+':
        print(f'The sum of your numbers is {sum}')

add(first_number, second_number)

def subtract(a, b):
    difference = a - b
    if operand == '-':
        print(f'The difference of your numbers is {difference}')

subtract(first_number, second_number)

def multiply(a, b):
    product = a * b
    if operand == '*':
        print(f'The product of your numbers is {product}')

multiply(first_number, second_number)

def divide(a, b):
    quotient = a / b
    if operand == '/':
        print(f'The quotient of your numbers is {quotient}')

divide(first_number, second_number)
