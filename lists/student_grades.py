infos = []

while True:
    name = str(input('Name: '))
    grade1 = float(input('Grade 1: '))
    grade2 = float(input('Grade 2: '))

    average = (grade1 + grade2)/2
    infos.append([name, [grade1, grade2], average])

    keep = str(input('Do you want to continue? (Y/N): ')).upper()
    if keep == 'N':
        break

print('-'*35)
print(f'{"Nu.":<6}{"NAMES":<10}{"AVERAGES":>8}')
print('-'*35)

for i, s in enumerate(infos):
    print(f'{i:<6}{s[0]:<10}{s[2]:>7.2f}')

while True:
    print('-'*35)
    specific = int(input('Show grades of which student? (999 interrupt): '))
    if specific == 999:
        break
    else:
        print(f"{infos[specific][0]}'s grades are: {infos[specific][1]}")