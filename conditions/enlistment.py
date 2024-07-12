from datetime import date

birth_year = int(input())
current_year = date.today().year
age = current_year - birth_year

missing = 18 - age
passing = age - 18

if age < 18:
    print(f'You are {age} years old. {missing} years left until you enlist.')
elif age == 18:
    print(f'You are {age} years old. Its time to enlist.')
elif age > 18:
    print(f'You are {age} years old. You are {passing} years late.')