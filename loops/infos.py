cont_average = 0
older_age = 0
older_name = ''
count_women = 0
for i in range(1,5):
    name = str(input(f'Name {i}: '))
    age = int(input(f'Age {i}: '))
    gender = str(input(f'Gender(M/F) {i}: '))

    cont_average += age
    
    if i == 1 and gender == 'M':
        older_age = age
        older_name = name
    if gender == 'M' and age > older_age:
        older_age = age
        older_name = name
    if gender == 'F' and age < 20:
        count_women += 1

average_ages = cont_average / 4

print(f'The age average in the group is {average_ages}.')
print(f'The older man in the group is {older_name}.')
print(f'There are {count_women} women under 20 years old.')