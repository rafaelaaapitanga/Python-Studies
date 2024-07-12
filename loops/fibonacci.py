terms = int(input())

count = 0
t1 = 0
t2 = 1
print(f'{t1}, {t2}, ', end='')

# t1 t2 t3 t4 t5 t6... tn
# 0  1  2  3  5  8
while count != terms-2: # there are 2 terms printed already (0, 1)
    tn = t1 + t2
    count += 1
    t1 = t2
    t2 = tn
    print(f'{tn}', end='')
    print(f', ' if count < terms-2 else '.', end='')