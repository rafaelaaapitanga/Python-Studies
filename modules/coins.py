def factorial(num):
    f = 1
    for c in range(1, num+1):
        f *= c
    return f

def double(num):
    return num*2

def half(num):
    return num/2

def increase(num, rate):
    inc = (num*(rate/100))+num
    return inc

def reduction(num, rate):
    disc = num-(num*(rate/100))
    return disc

def general(p, ratei, rated):
    print('-'*30)
    print('SUMMARY'.center(30))
    print('-'*30)
    print(f'Value analyzed: {p}')
    print(f'Double: {double(p)}')
    print(f'Factorial: {factorial(p)}')
    print(f'Half: {half(p)}')
    print(f'{ratei}% increase: {increase(p, ratei)}')
    print(f'{rated}% reduction: {reduction(p, rated)}')
    print('-'*30)