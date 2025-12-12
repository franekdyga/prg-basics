grades = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]

grades2 = list(filter(lambda x:x>2, grades))

sum = 0
for x in grades2:
    sum += x
result = sum/len(grades2)

print(round(result, 2))