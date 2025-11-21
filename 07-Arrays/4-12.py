categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

counter = 0
most_expensive = ''

for i in range(len(categories)):
    if expenses[i] > counter:
        counter = expenses[i]
        most_expensive = categories[i]
print(most_expensive)