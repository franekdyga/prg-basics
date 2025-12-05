###
# Checks the correctness of username and password
#
import re

# read username and password from keyboard
username = str(input('Podaj login: '))
password = str(input('Podaj haslo: '))

# pattern (criteria) for username and password
username_pattern = '\w{5,}[a-z]'
password_pattern = '\w{7,}[a-zA-Z1-9_]'

# check if username and password are ok
username_match = re.match(username_pattern,username)
password_match = re.match(password_pattern,password)

# print results
if username_match and password_match:
   print(f'Okej, login: {username}, haslo: {password}')
else:
   print(f'nie')