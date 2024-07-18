array = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(3): # lines
    for c in range(3): # columns
        array[l][c] = int(input(f'Enter a number for position [{l}, {c}]: '))

for l in range(3):
    for c in range(3):
        print(f'[{array[l][c]:^5}]', end='') # centralize
    print()

even = third_column = highest = 0
for l in range(3):
    third_column += array[l][2]
    for c in range(3):
        if array[l][c] % 2 == 0:
            even += array[l][c]

        if c == 0:
            highest = array[1][c]
        elif array[1][c] > highest:
            highest = array[1][c]

#scnd_line_num = []
#for c in range(3):
#    scnd_line_num.append(array[1][c])
#highest = max(scnd_line_num)

print(f'Sum of all even numbers: {even}')
print(f'Sum of numbers in the third column: {third_column}')
print(f'The highest number in the second line: {highest}')