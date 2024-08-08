def readInt(numb):
    while True:
        n = str(input(numb))
        if n.isnumeric():
            print(f'You entered the number {n}')
            break
        else:
            print('ERRO.')

readInt('Enter a number: ')