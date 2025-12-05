
file_name = 'it_company.csv'

list = []

counter = 0
list_counter = 0

with open(file_name, 'r') as file:
    for line in file:
        list.append(line)
list.pop(0)

limit = (len(list)/5)
limit_counter = 0

while counter != 1:
    for i in range(0,5):
        print(list[list_counter])
        list_counter += 1
    counter += 1
    if counter == 1:
        input('Press Enter key to display next 5')
        counter = 0
        limit_counter += 1
    if limit_counter == (limit):
        break