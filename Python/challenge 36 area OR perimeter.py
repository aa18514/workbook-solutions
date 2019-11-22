def area(length, width):
    shapeArea = length * width
    print("Area = ",shapeArea)


def perimeter(length, width):
    shapePerimeter = length*2 + width*2
    print ("Perimeter = ", shapePerimeter)

def volume(length, width, height):
    volume = length * width * height
    print("Volume = ", volume)

length = int(input ("Enter the length of the rectangle"))
width = int(input ("Enter the width of the rectangle"))
height = int(input ("Enter the height of the rectangle"))

response = None

while response not in ("a","p", "v"):
    response = input("Do you want to calculate area or perimeter or volume? Enter a or p or v")
    response = response.lower()

if response == "a":
    area(length, width)

elif response == "p":
    perimeter(length, width)

elif response == 'v':
    
    volume(length, width, height)


