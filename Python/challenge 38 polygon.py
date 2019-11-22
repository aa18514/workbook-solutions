import turtle
wn = turtle.Screen()
tom = turtle.Turtle()
tom.pendown()
def polygon (sides, length):
    angle = 360/sides
    for sides in range (sides):
        tom.forward(length)
        tom.right(angle)
        

polygon (360, 1)
wn.exitonclick()
