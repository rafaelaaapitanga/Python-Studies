numbers = [[], []]

for i in range(7):
    number = int(input(f'Enter the value {i+1}: '))
    
    if number % 2 == 0:
        numbers[0].append(number) # even
    else:
        numbers[1].append(number) # odd

numbers[0].sort()
numbers[1].sort()
print(f'List of even numbers in ascending order: {numbers[0]}')
print(f'List of odd numbers in ascending order: {numbers[1]}')