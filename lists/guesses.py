from random import randint
from time import sleep

games = int(input('How many games do you want to draw? '))

for i in range(games):
    guesses = []
    for j in range(6):
        numbers = randint(1,60)
        if numbers not in guesses:
            guesses.append(numbers)

    print(f'Game {i+1}: {guesses}')
    sleep(0.7)