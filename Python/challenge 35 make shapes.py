import turtle
wn = turtle.Screen()
tom = turtle.Turtle()
tom.pendown()
def square(length):
    for a in range (4):
        tom.forward(length)
        tom.right(90)
    

def triangle(length):
    for a in range (3):
        tom.forward(length)
        tom.right(120)
    

def rectangle(length, width):
    for a in range (2):
        tom.forward(length)
        tom.right(90)
        tom.forward(width)
        tom.right(90)
   

def polygon(numsides, length):
    for a in range (numsides):
        tom.forward(length)
        tom.right(360/numsides)
   
length = int(input("Enter the length"))
width = int(input("Enter the width"))
rectangle(length, width)
wn.exitonclick()

#triangle(size)
#square(size)

#polygon(5, size)


