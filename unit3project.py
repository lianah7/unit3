# by Liana Hill
# last updated October 1, 2019
# this program calculates the total surface area of a rectangular prism

def purpose_of_program():
    print("This program calculates the total surface area of a rectangular prism")
    print("Please enter the length, width, and height of the rectangle")

def input_length():
    length = float(input("What is the length of the rectangle?"))
    return length

def input_width():
    width = float(input("What is the width of the rectangle?"))
    return width

def input_height():
    height = float(input("What is the height of the rectangle?"))
    return height

def area_of_rectangle(length, width):
    area = length * width
    return area

def surface_area(length, width, height):
    surface = length * width * height
    return surface

def main():
    purpose_of_program()
    area = input_width() * input_length()
    surface = input_length() * input_width() * input_height()