number = int(input())

mult = number
factorial = 1

while mult > 0:
    print(f'{mult} ', end='')
    print('x ' if mult > 1 else '= ', end='')
    factorial *= mult
    mult -= 1
print(factorial)