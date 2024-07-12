n1 = int(input())
n2 = int(input())
n3 = int(input())

highest = n3
if n1 > n2 and n1 > n3:
    highest = n1
elif n2 > n1 and n2 > n3:
    highest = n2

lowest = n3
if n1 < n2 and n1 < n3:
    lowest = n1
elif n2 < n1 and n2 < n3:
    lowest = n2

print(f'Highest number: {highest}')
print(f'Lowest number: {lowest}')