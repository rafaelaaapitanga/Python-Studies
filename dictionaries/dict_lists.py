info_list = []
count = 0
count_age = 0

while True:
    info_dict = {'name': str(input('Name: ')),
                 'gender': str(input('Gender [M/F]: ')).upper(),
                 'age': int(input('Age: '))}
    info_list.append(info_dict)
    count += 1
    count_age += info_dict['age']
    keep = str(input('Do you want to add more informations? [Y/N]: ')).upper()
    if keep == 'N':
        break

average_age = count_age/count
print(f'{count} people were registered.') # total
print(f'The average age is {average_age}') # average age

women = []
old_people = []
for i, v in enumerate(info_list):
    if v['gender'] == 'F':
        women.append(v['name'])
    if v['age'] > average_age:
        old_people.append(v)

print('The women registered were ', end='')
for i in range(len(women)):
    print(f'{women[i]} ', end='') # women registered

print(f'\nList of people above average age: ', end='') # above average age
print(f'\n{old_people}')