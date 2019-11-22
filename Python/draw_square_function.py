import turtle
wn = turtle.Screen()
tom = turtle.Turtle()

def draw_square():		  # define our new function in this format
    for sides in range (4): # all code is indented to show its part of the for loop
        tom.forward(150)	
        tom.right(90)

draw_square()			  # call the function with this command
