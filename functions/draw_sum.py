from random import randint
list_numbers = []

def draw():
    for i in range(5):
        list_numbers.append(randint(1, 10))

def sum_even():
    draw()
    sum = 0
    print('Drawn numbers:', end=' ')
    for i in list_numbers:
        print(i, end=' ')
        if i % 2 == 0:
            sum += i
    print(f'\nSum of even numbers: {sum}')

sum_even()