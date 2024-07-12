from random import randint

attempt = int(input('Try a number: '))
num = randint(0,10)
count = 1

while attempt != num:
    count += 1
    if attempt > num:
        attempt = int(input('Try a smaller number.\n'))
    elif attempt < num:
        attempt = int(input('Try a bigger number.\n'))

print(f'The number was {num}. You got it with {count} tries!')