info_player = {}

info_player['name'] = input('Football player name: ')
info_player['matches'] = int(input('Football game matches: '))

goals_per_match = []
count_goals = 0

for match in range(info_player['matches']):
    goals = int(input(f'How many goals in match {match+1}? '))
    goals_per_match.append(goals)
    count_goals += goals

info_player['total goals'] = count_goals
print(info_player)

for k, v in info_player.items():
    print(f'{k} = {v}')

print(f"{info_player['name']} played {info_player['matches']} matches.")
for i, goals in enumerate(goals_per_match):
    print(f'In match {i+1}, he scored {goals} goals.')