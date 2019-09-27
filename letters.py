# by Liana Hill
# last updated by September 27, 2019
# creating a font and spelling Mississippi

import turtle
turtle.speed(3)

turtle.penup()
turtle.goto(-450,0)
turtle.pendown()

def goto(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

# M function
def make_m():
    turtle.seth(90)
    turtle.fd(90)
    turtle.rt(135)
    turtle.fd(40)
    turtle.lt(95)
    turtle.fd(40)
    turtle.rt(140)
    turtle.fd(90)

def make_i():
    turtle.lt(90)
    turtle.fd(20)
    turtle.lt(180)
    turtle.fd(10)
    turtle.rt(90)
    turtle.fd(90)
    turtle.left(90)
    turtle.fd(10)
    turtle.rt(180)
    turtle.fd(20)

def make_s():
    turtle.rt(90)
    for x in range(5):
        turtle.fd(20)
        turtle.lt(45)
    turtle.fd(40)

make_m()
goto(-375, 0)
make_i()
goto(-345, 30)
make_s()

turtle.exitonclick()