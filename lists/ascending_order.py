list_numbers = []

while True:
    num = int(input('Enter a number: '))
    if num not in list_numbers:
        list_numbers.append(num)

    keep = input('Do you want to add more numbers? (y/n) ').strip().lower()
    if keep == 'n':
        break

list_numbers.sort()
print(list_numbers)