vel = int(input())

fine = 7*(vel-80)

if vel > 80:
    print(f'You were fined! You will have to pay ${fine}')
else:
    print('No fines. Good.')