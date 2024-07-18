data = []

while True:
    people = []
    people.append(str(input('Name: ')))
    people.append(float(input('Weight: ')))
    data.append(people)

    keep = str(input('Do you want to add more information? (y/n) '))
    if keep == 'n':
        break

print(f'{len(data)} people are registered')

heaviest = []
lighest = []
heavy = light = data[0][1]

for person in data:
    weight = person[1]

    if weight > heavy:
        heavy = weight
        heaviest = [person[0]]
    elif weight == heavy:
        heaviest.append(person[0])

    if weight < light:
        light = weight
        lighest = [person[0]]
    elif weight == light:
        lighest.append(person[0])

print(f'The heaviest person(s) is/are: {heaviest} with {heavy} kg.')
print(f'The lighest person(s) is/are: {lighest} with {light} kg.')