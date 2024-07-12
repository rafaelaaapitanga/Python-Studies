dist = int(input())

if dist <= 200:
    cost = 0.5*dist
    print(f'Cost: {cost}')
else:
    cost = 0.45*dist
    print(f'Cost: {cost}')