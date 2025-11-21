###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print('Last value', arr[-1])
print('Last but one value', arr[4])
print('Sum of thhe first and last value', arr[0]+arr[-1])
a = int((len(arr)-1)/2)
print('Middle value', arr[a])

for i in range(len(arr)):
    print(arr[i], end=" ")