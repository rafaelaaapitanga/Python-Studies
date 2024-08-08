def grades(* grade):
    count = 0
    sum = 0
    dic = {}
    list_grades = []
    for g in grade:
        list_grades.append(g)
        count += 1
        dic['total'] = count
        dic['highest'] = max(list_grades)
        dic['smallest'] = min(list_grades)
        sum += g
        dic['average'] = sum/count

        if dic['average'] >= 7:
            dic['situation'] = 'GOOD'
        elif 5 < dic['average'] < 7:
            dic['situation'] = 'REASONABLE'
        else:
            dic['situation'] = 'BAD'

    print(dic)

grades(5, 9, 10, 9.5)