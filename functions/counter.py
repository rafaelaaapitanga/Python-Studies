def count(beginning, end, passing):
    print(f'Count from {beginning} to {end} by {passing}:')

    if beginning < end:
        c = beginning # count
        while c <= end:
            print(f'{c}', end=' ')
            c += passing
        print()
    else:
        c = beginning
        while c >= end:
            print(f'{c}', end=' ')
            c -= passing
        print()

count(1, 10, 1)
count(10, 0, 2)
print('=~'*20)

print('Now you can customize your count!')
s = int(input('Start: '))
e = int(input('End: '))
p = int(input('Pass: '))

count(s, e, p)