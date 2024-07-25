info_list = []

while True:
    goals_per_match = []
    total_goals = 0
    info_player = {}

    info_player['name'] = input('Football player name: ')
    matches = int(input('Football game matches: '))
    for match in range(matches):
        goals = int(input(f'How many goals in match {match+1}? '))
        goals_per_match.append(goals)
        total_goals += goals
    info_player['goals'] = goals_per_match
    info_player['total'] = total_goals

    info_list.append(info_player)
    
    keep = str(input('Do you want to add more players? [Y/N] ')).upper()
    if keep == 'N':
        break

print('cod ', end='')
for i in info_player.keys():
    print(f'{i:<17}', end='')
print()
print('-'*60)

for k, v in enumerate(info_list):
    print(f'{k:>2} ', end='')

    for d in v.values():
        print(f'{str(d):<18}', end='')
    print()
print('-'*60)

while True:
    search = int(input('What player do you want to see the informations? [999 to interrupt] '))
    if search == 999:
        break
    else:
        print(f"Informations about the player {info_list[search]['name']}:")
        for i, g in enumerate(info_list[search]['goals']):
            print(f"In match {i+1}, {info_list[search]['name']} scored {g} goals.")
