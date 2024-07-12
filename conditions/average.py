n1 = float(input())
n2 = float(input())

average = (n1+n2)/2

if average < 5:
    print('Disapproved!')
elif 5 < average < 6.9:
    print('Retake!')
elif average >=7:
    print('Approved!')