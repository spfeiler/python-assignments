user_number = int(input('Enter Number Here: '))

if user_number > 1:
    for index in range(2, user_number):
        if user_number % index == 0:
            print('Your number is not a prime number.')
            break
    else:
        print('Your number is a prime number.')
else:
    print('Your number is not a prime number.')
