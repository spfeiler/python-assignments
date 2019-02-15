# Assignment 1:

names = ['Alex', 'John', 'Mary', 'Steve', 'John', 'Steve']

def remove_duplicates(names):
    updated_names = []
    for name in names:
        if name not in updated_names:
            updated_names.append(name)
    return updated_names

print(remove_duplicates(names))

# Assignment 2:

numbers = [100, 3, 6, 8, 82, 27, 59, 1, 52]

def largest_number(numbers):
    numbers.sort()
    print(numbers[-1])

largest_number(numbers)

# Assignment 3:

def smallest_number(numbers):
    numbers.sort()
    print(numbers[0])

smallest_number(numbers)

# Assignment 4:

numbers_2 = [0, 1, 2, 3, 4, 6, 7, 8, 9]

def find_missing_number(numbers_2):
    for i in numbers_2:
        x = i * (i + 1) / 2
        sum_of_numbers = sum(numbers_2)
    return x - sum_of_numbers

print(find_missing_number(numbers_2))

# Assignment 5:

numbers_3 = [1, 2, 3, 4, 5]

def duplicate_numbers(numbers_3):
    duplicates = []
    for i in numbers_3:
        duplicates.append(i)
    for i in duplicates:
        numbers_3.append(i)
    return numbers_3

print(duplicate_numbers(numbers_3))
