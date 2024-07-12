from random import randint
print('''Your options:
[1] paper
[2] scissors
[3] rock''')

you = int(input('What is your choice? '))
pc = randint(1,3)

if you == 1:
    print('You chose paper.')
elif you == 2:
    print('You chose scissors.')
elif you == 3:
    print('You chose rock.')

if you == 1 and pc == 1:
    pc = 'paper'
    print(f'PC chose {pc}. TIE!')
elif you == 2 and pc == 2:
    pc = 'scissors'
    print(f'PC chose {pc}. TIE!')
elif you == 3 and pc == 3:
    pc = 'rock'
    print(f'PC chose {pc}. TIE!')
elif you == 1 and pc == 2:
    pc = 'scissors'
    print(f'PC chose {pc}. You lost!')
elif you == 1 and pc == 3:
    pc = 'rock'
    print(f'PC chose {pc}. You won!')
elif you == 2 and pc == 1:
    pc = 'paper'
    print(f'PC chose {pc}. You won!')
elif you == 2 and pc == 3:
    pc = 'rock'
    print(f'PC chose {pc}. You lost!')
elif you == 3 and pc == 1:
    pc = 'paper'
    print(f'PC chose {pc}. You lost!')
elif you == 3 and pc == 2:
    pc = 'scissors'
    print(f'PC chose {pc}. You won!')