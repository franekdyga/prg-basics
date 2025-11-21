###
# Functions to read any data type from the keyboard
#
def input_string(message):
    a = input(message)
    return str(a)

def input_integer(message):
    b = input(message)
    return int(b)

def input_real(message):
    c = input(message)
    return float(c)

def input_boolean(message):
    d = input(message)
    return str(d)

###
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed
#
# import keyboard # your own defined module

# Reads employee's data from keyboard
first_name = input_string('Enter name: ')
last_name = input_string('Enter surname: ')
age = input_integer('Enter age: ')
salary = input_real('Enter salary: ')
is_salary_hidden = input_boolean('Hide salary? (y/n): ')

# Prints employee's record
print('DATA RECORD')
print('===========')
print(f'Name and surname: {first_name} {last_name}')
print(f'Age: {age}')
if is_salary_hidden == 'n':
    print('Salary')