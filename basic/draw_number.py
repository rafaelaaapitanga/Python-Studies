import random

s1 = str(input())
s2 = str(input())
s3 = str(input())
s4 = str(input())

list = [s1, s2, s3, s4]
chosen = random.choice(list)

print(f'The chosen student is {chosen}')