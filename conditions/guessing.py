from random import randint

random_num = randint(0, 5)
number = int(input('Enter a number between 0 and 5: '))

if number == random_num:
    print(f'You won! The number drawn was {random_num}.')
else:
    print(f'You failed! The number drawn was {random_num}.')