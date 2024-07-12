while True:
    number = int(input())

    if number > 0:
        for i in range(11):
            print(f'{i} x {number} = {i*number}')
    else:
        break

print('Program closed.')