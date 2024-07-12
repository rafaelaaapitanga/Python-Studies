from datetime import date

count_old = 0
count_young = 0
for i in range(7):
    births = int(input())
    ages = date.today().year - births
    
    if ages >= 18:
        count_old += 1
    else:
        count_young += 1

print(f'{count_old} people are major and {count_young} people are minor.')
