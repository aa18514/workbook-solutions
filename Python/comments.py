# this program creates a random number between 1 and 10
# the user guesses the number. It ends when the user guesses the number correctly
import random
guess =""
print ("I've thought of a number between 1 and 10. Try to guess it.")
randomNumber = random.randrange (1,10)
# this loop runs until the number guessed equals the randomNumber
while guess != randomNumber:
    guess = int(input("Guess the number"))
    print("You got it wrong")

input ("Well done. Press any key to exit.")
