general = []

while True:
    num = int(input())
    general.append(num)

    keep = str(input('Do you want to add more numbers? (y/n) '))
    if keep == 'n':
        break

even = []
odd = []

for num in general:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print(f'General list: {general}')
print(f'Even list: {even}')
print(f'Odd list: {odd}')