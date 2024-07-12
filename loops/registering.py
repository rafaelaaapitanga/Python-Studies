count_18 = 0
count_men = 0
count_women = 0

while True:
    age= int(input('Age? '))
    gender = str(input('Gender? M/F ')).upper()
    keep = str(input('Continue? y/n '))

    if age > 18:
        count_18 += 1
    if gender == 'M':
        count_men += 1
    if gender == 'F' and age < 20:
        count_women += 1
    if keep == 'n':
        break

print(f'{count_18} people are over 18 years old.')
print(f'{count_men} men were registered.')
print(f'{count_women} women are under 20 years old.')