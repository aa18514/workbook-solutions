import turtle
wn = turtle.Screen()
tom = turtle.Turtle()                        # create a turtle called tom



def draw_square(boundary_color, fill_color): # define our new function in this format
     tom.color(boundary_color, fill_color)
     tom.begin_fill()
     for sides in range (4): 
        tom.forward(150)	
        tom.right(90)
     tom.end_fill()




outline = input('What color outline should I draw?')
fill = input('What colour should I use to fill the shape?')   
