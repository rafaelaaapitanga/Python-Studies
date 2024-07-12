number = int(input())

count = 0
for i in range(1, number+1):
    if (number % i) == 0:
        count += 1

if count > 2:
    print(f'{number} is not a prime number. Its divisible by {count} numbers.')
elif count == 2:
    print(f'{number} is a prime number. Its only divisible by 1 and itself.')