# by Liana Hill
# last updated October 1, 2019
# this program calculates the total surface area of a rectangular prism


def purpose_of_program():
    """
    This function tells the user what the program does
    :return:
    """
    print("This program calculates the total surface area of a rectangular prism")
    print("Please enter the length, width, and height of the rectangle")


def input_length():
    """
    This function asks the user for the length of the rectangle
    :return: the user gives the length
    """
    return float(input("What is the length of the rectangle?"))


def input_width():
    """
    This function asks the user to pick a width for the rectangle
    :return: the user gives the width
    """
    return float(input("What is the width of the rectangle?"))


def input_height():
    """
    This function asks the user for a height of the rectangle
    :return: the user gives the height
    """
    return float(input("What is the height of the rectangle?"))


def area_of_rectangle(length, width):
    """
    This function calculates the area of the rectangle
    :param length: the length of the rectangle
    :param width: the width of the rectangle
    :return: the length times the width
    """
    return length * width


def surface_area(length, width, height):
    """
    This function calculates the total surface area of the rectangular prism
    :param length: the length of the rectangle
    :param width: the width of the rectangle
    :param height: the height og the rectangle
    :return: each area of a side times two, all added together
    """
    return (area_of_rectangle(length, width) * 2) + (area_of_rectangle(length, height) * 2) + \
           (area_of_rectangle(width, height) * 2)


def main():
    purpose_of_program()
    length = input_length()
    width = input_width()
    height = input_height()
    print("The total surface area is", surface_area(length, width, height))


main()
