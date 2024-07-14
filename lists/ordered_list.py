numbers = []

for i in range(5):
    num = int(input("Enter a number: "))
    
    if i == 0:
        numbers.append(num) # only for the first number
    else:
        numbers.append(num)
        while i > 0 and numbers[i] < numbers[i - 1]:
            numbers[i], numbers[i - 1] = numbers[i - 1], numbers[i] # swap
            i -= 1

print(numbers)