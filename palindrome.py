user_word = input('Enter Word Here: ').lower()
reversed_word = ""

for index in range(len(user_word)-1, -1, -1):
    reversed_word += user_word[index]

if user_word == reversed_word:
    print('Your word is a palindrome')
else:
    print('Your word is not a palindrome')
