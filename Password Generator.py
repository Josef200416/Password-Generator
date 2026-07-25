import random
import string
characters = string.ascii_letters + string.digits + string.punctuation
while True:
    while True:
        try:
            length = int(input('Length: '))
            if 4 <= length <= 32:
                break
            else:
                print ('Please pick a number between 4 and 32')
        except ValueError:
         print('Please enter a number.')
    password = ''
    for i in range(length):
        password = password + random.choice(characters)
    print(password)
    again = input ('Press Enter for another, or q to quit: ')
    if again == 'q':
        break