# banknotes available: 50, 20, 10, 1
value = int(input('The amount to be withdrawn? '))
total = value
money = 50 # higher value at the atm
total_money = 0

while True:
    if total >= money:
        total -= money
        total_money += 1
    else:
        if total_money > 0:
            print(f'{total_money} ${money} bills will be required')
        if money == 50:
            money = 20
        elif money == 20:
            money = 10
        elif money == 10:
            money = 1
        total_money = 0

        if total == 0:
            break