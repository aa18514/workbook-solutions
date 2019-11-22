# Enter a number between 1 and 10
number = 100
while number not in range (1,11): ## number not in between 1 and 10
    try:
        number = int(input("Please enter a number between 1 and 10"))
    except:
        print("ERROR invalid input. Wrong type of data.")
print("Thank you I have recorded your entry as :", number)

