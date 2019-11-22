import turtle
wn = turtle.Screen()                        #opens a new canvas for the drawing
tom = turtle.Turtle()                        # create a turtle pen called tom

def draw_square(boundary_color, fill_color, bg_color): # define our function. It takes two arguments or inputs: boudnary_color and fill_color.
     wn.bgcolor(bg_color)
     tom.color(boundary_color, fill_color)  # the color of the turtle tool is set
     tom.begin_fill()                        
     for sides in range (4):                #This for loop draws the square
        tom.forward(150)	
        tom.right(90)
     tom.end_fill()
     turtle.exitonclick()



bg_color = input('What background color do you want?')
fill = input('What color should the square be filled with?')
boundary = input('What color outline should the square have?')


draw_square(boundary, fill, bg_color)			     
