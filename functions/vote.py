def vote(year):
    from datetime import date
    actual = date.today().year
    age = actual-year

    if age < 16:
        print(f'{age} years. Vote denied!')
    elif 18 <= age <= 70:
        print(f'{age} years. Mandatory vote!')
    elif age > 70 or 16 <= age < 18:
        print(f'{age} years. Optional vote!')

year_birth = int(input('Year of birth: '))
vote(year_birth)