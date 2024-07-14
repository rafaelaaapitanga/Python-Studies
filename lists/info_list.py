numbers = []

while True:
    num = numbers.append(int(input('Enter a number: ')))
    keep = str(input('Do you want to add more numbers? (y/n) '))

    if keep == 'n':
        break

numbers.sort(reverse=True)
print(f'List in descending order: {numbers}')
print(f'There are {len(numbers)} numbers in the list')

if 5 in numbers:
    print('Number 5 is in the list.')
else:
    print('Number 5 is not in the list.')