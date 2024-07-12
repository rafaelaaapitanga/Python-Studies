words = ('ball', 'cup', 'handsome', 'beautiful', 'computer', 'television')
vowels = 'aeiou'

count = 0

for word in words:
    print(f'\nThe word {word} has the vowels ', end='')
    for letter in word:
        if letter in vowels:
            print(f'{letter}', end=' ')