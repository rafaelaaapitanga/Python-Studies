from random import randint
from operator import itemgetter

plays = {'p1': randint(1, 6),
         'p2': randint(1, 6),
         'p3': randint(1, 6),
         'p4': randint(1, 6)}

for k, v in plays.items():
    print(f'{k} got {v}')

ranking = sorted(plays.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'{i+1} place: {v[0]} with number {v[1]}')