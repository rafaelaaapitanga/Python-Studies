from random import randint
count = 0

while True: # while youre winning
    value = int(input('Choose a value: '))
    odd_even = str(input('Odd or even? O/E ')).upper()
    pc = randint(0,10)
    sum = value + pc
    
    if odd_even == 'E' and sum%2 == 0:
        print(f'You won! You chose {value} and pc chose {pc}. The sum is {sum}, even number!')
        count += 1
    elif odd_even == 'O' and sum%2 != 0:
        print(f'You won! You chose {value} and pc chose {pc}. The sum is {sum}, odd number!')
        count += 1
    elif odd_even == 'O' and sum%2 == 0:
        print(f'You lost! You chose {value} and pc chose {pc}. The sum is {sum}, even number!')
        break
    elif odd_even == 'E' and sum%2 != 0:
        print(f'You lost! You chose {value} and pc chose {pc}. The sum is {sum}, odd number!')
        break

print(f'You won {count} times!')