user_number = int(input('Enter Number Here: '))
factorial = 1

while user_number > 0:
    factorial = factorial * user_number
    user_number = user_number - 1

print(factorial)
