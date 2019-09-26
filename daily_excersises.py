# by Liana Hill
# September 25, 2019
# daily exercises classwork

# the following functions create the tops and bottoms for hexagons


def make_top_of_hexagon():
    print("  __________  ")
    print(" /          \\ ")
    print("/            \\")


def make_bottom_of_hexagon():
    print("\\            /")
    print(" \\__________/")


def make_line_of_punctuation():
    print("  -\"-\'-\"-\'-\"-")

# the following functions are to sing happy birthday


def happy_birthday_to_you():
    print("Happy birthday to you")


def happy_birthday(name):
    print("Happy birthday dear", name)


def adding_numbers(number1, number2):
    return number1 + number2


def main():
    make_top_of_hexagon()
    make_bottom_of_hexagon()
    make_line_of_punctuation()
    make_top_of_hexagon()
    make_bottom_of_hexagon()
    make_line_of_punctuation()
    make_bottom_of_hexagon()
    make_top_of_hexagon()
    make_line_of_punctuation()
    make_bottom_of_hexagon()
    happy_birthday_to_you()
    happy_birthday_to_you()
    happy_birthday("Mom and Pops")
    happy_birthday_to_you()
    answer = adding_numbers(4, 6)
    print("The answer is", answer)


main()