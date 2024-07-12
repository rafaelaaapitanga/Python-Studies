sentence = str(input()).strip().upper()

words = sentence.split()
joining = ''.join(words)
size = len(joining)

inverse = ''
for letter in range(size-1, -1, -1): # returning
    inverse += joining[letter]

if joining == inverse:
    print(f'The sentence is a palindrome! ({joining} = {inverse})')
else:
    print(f'The sentence is not a palindrome. ({joining} != {inverse})')

# you could also just use "inverse = junto[::-1]"