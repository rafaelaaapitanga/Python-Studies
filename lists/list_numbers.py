list_numbers = []
largest = 0
smallest = 0
pos_smallest = 0
pos_largest = 0

for i in range(5):
    list_numbers.append(int(input(f'Enter a number in position {i+1}: ')))

    if i == 0: # only for the first position
        largest = smallest = list_numbers[0] # largest and smallest will get the first number
    else:
        if list_numbers[i] > largest:
            largest = list_numbers[i]
            pos_largest = i
        elif list_numbers[i] < smallest:
            smallest = list_numbers[i]
            pos_smallest = i

print(f'The largest number is {largest} in position {pos_largest+1}')
print(f'The smallest number is {smallest} in position {pos_smallest+1}')