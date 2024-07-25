students = {}
students['name'] = str(input('Name: '))
students['average'] = float(input('Average: '))

if students['average'] >= 7:
    students['situation'] = 'approved'
elif 6 <= students['Average'] < 7:
    students['situation'] = 'recovery'
else:
    students['situation'] = 'failed'

for k, v in students.items(): # key and value
    print(f'Your {k} is {v}')