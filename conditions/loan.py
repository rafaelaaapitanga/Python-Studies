home = int(input('Home value: '))
salary = int(input('Salary: '))
years = int(input('Years to pay: '))

# monthly installment can't exceed 30% of the salary
installment = home/(years*12)
limit_monthly = 0.3*salary

if installment > limit_monthly:
    print(f'Loan denied! Your installment of {installment:.2f} exceeded the limit of {limit_monthly}')
else:
    print(f'Loan approved! You will have to pay {installment:.2f} per month.')