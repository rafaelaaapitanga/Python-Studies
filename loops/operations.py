n1 = int(input())
n2 = int(input())

print('''Choose: [1] sum
        [2] multiply
        [3] bigger
        [4] new numbers
        [5] exit ''')

start = True
while start:
    option = int(input())
    if option == 1:
        print(f'{n1} + {n2} = {n1+n2}')
    elif option == 2:
        print(f'{n1} x {n2} = {n1*n2}')
    elif option == 3:
        if n1 > n2:
            print(f'{n1} is the biggest one.')
        else:
            print(f'{n2} is the biggest one.')
    elif option == 4:
        n1 = int(input())
        n2 = int(input())
    elif option == 5:
        start = False
    else:
        print('Invalid option. Try again.')

print('End of the program.')