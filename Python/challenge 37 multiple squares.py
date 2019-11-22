# coordinates in the turtle library
import turtle           # import turtle module
wn = turtle.Screen()    # make a graphics window to draw in
wn.setup(500, 500)
tom = turtle.Turtle()   # create a turtle called tom

def square(length):
    for sides in range (4):
        tom.forward(length)
        tom.right(90)

tom.penup()
tom.goto(0, 200)
tom.pendown()
square(100)
tom.penup()


tom.goto(-200, 0)
tom.pendown()
square(100)
tom.penup()

tom.goto(100, 0)
tom.pendown()
square(100)
tom.penup()

tom.goto(0, -100)
tom.pendown()
square(100)
tom.penup()

wn.exitonclick()
