# by Liana Hill
# September 26, 2019
# daily exercises number 5

import math
def triangle_sides(a, b, c):
    s = (a + b + c)/2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    return area

def main():
    a = int(input("WHat is the length of the first side?"))
    b = int(input("WHat is the length of the second side?"))
    c = int(input("WHat is the length of the third side?"))
    answer = triangle_sides(a, b, c)
    print("The area of the triangle is", answer)

main()
