from random import randint
numbers = (randint(1,30), randint(1,30), randint(1,30), randint(1,30), randint(1,30))

print(f'Generated numbers: ', end='')
for i in numbers:
    print(f'{i} ', end='')

print(f'\nThe highest number is {max(numbers)}')
print(f'The smallest number is {min(numbers)}')