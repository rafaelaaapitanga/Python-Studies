gender = str(input()).upper()[0]

while gender not in 'FM':
    gender = str(input('Try again: ')).upper()[0]

print(f'{gender} registered.')