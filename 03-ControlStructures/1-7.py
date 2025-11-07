###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
basic_salary = 5000
total_salary = 0
bonus = 0.15 # 15%
is_bonus = input('Does the employee receive a bonus? (Y/N): ') 


if is_bonus == 'Y':
    total_salary = basic_salary+(basic_salary*bonus)
else:
    total_salary = basic_salary

print(f'Basic salary: {basic_salary}')
if is_bonus == 'Y':
    print('Bonus is included')
else:
    print('Bonus is not included')
    
print(f'Total salary: {total_salary}')