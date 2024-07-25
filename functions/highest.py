from time import sleep

def highest(* num):
    high = 0
    print('Analyzing the numbers: ')
    for v in num:
        print(f'{v}', end=' ', flush=True)
        sleep(0.6)
        if v > high:
            high = v
    print(f'\nThe highest number is {high}')
    print('=~'*20)


highest(3, 4, 5, 6)
highest(5, 5, 2, 1)
highest(100, 900, 3, 40, 1000, 1, 72)
highest(2)
highest()