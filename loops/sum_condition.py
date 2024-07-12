start = True
sum = 0

while start:
    num = int(input())

    if num != 999:
        sum += num
    else:
        start = False

print(sum)