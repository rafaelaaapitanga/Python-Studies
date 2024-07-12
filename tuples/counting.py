numbers = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten')
number = int(input())

while True:
    if number <= 10:
        print(f'You entered the number {numbers[number-1]}.')
        break
    else:
        print('Try again. Only numbers from one to ten.')
        number = int(input())