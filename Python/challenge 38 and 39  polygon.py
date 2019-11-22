import turtle
wn = turtle.Screen()
tom = turtle.Turtle()
tom.pendown()
def polygon (sides, length):
    angle = 360/sides
    for sides in range (sides):
        tom.forward(length)
        tom.right(angle)
        
##polygon (4, 80)
##polygon (5, 80)
##polygon (6, 80)
##polygon (7, 80)
        

polygon (360, 1)  
polygon (360, 0.5)
polygon (360, 0.25)
polygon (360, 0.125)

wn.exitonclick()
