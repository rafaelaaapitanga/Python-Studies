def factorial(num, show=False):
    fact = 1

    for i in range(num, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(f' x ', end='')
            else:
                print(f' = ', end='')

        fact *= i
    print(fact)

factorial(5, show=True)
factorial(5, show=False)