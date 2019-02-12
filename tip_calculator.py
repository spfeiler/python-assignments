total_amount = int(input('Enter Total Amount'))
tip_percentage = int(input('Enter Tip Percentage'))

def calculate_tip(a, b):
    return((a * b) / 100)

tip_amount = calculate_tip(total_amount, tip_percentage)
print(f'The tip amount is ${tip_amount}.')
