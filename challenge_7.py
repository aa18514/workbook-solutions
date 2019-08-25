'''
Challenge 7 - Area Calculator:
A program that asks the user for the width and the height
of a room and calculates the area of the room.
'''


# length and width can be decimal numbers!
length = float(input("what is the length of the room?\n"))
width = float(input("what is the width of the room?\n"))

# calculate area of the room
area = length * width


# display the area of the room
print ("Area of the room is: "  + area)
