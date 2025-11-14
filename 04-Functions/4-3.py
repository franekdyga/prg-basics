###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math

def triangle_area(a,b,c):
    s = 1/2*(a+b+c)
    p = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return p

print(f'The area of ​​a triangle with sides 3, 4, 5 is {int(triangle_area(3, 4, 5))}')
print(f'The area of ​​a triangle with sides 5, 12, 13 is {int(triangle_area(5, 12, 13))}')
print(f'The area of ​​a triangle with sides 7, 24 ,25 is {int(triangle_area(7, 24, 25))}')