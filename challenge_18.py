'''
Challenge 8 - Magic8Ball

Provide students with an answer to any question that they ask the computer.
Introduces students to if-else statements!
'''

import random

answer1="Absolutely!"
answer2="No way!"
answer3="I really don't care."

print("Welcome to the Magic 8 Ball game -- use it to answer your questions...")

question=input("Ask me for any advice and I'll help you out. Type in your question\
        and then press Enter for an answer.")

print("shaking.... \n" * 4)

choice = random.randint(1, 3) #chooses a random integer between 1 and 3

if choice == 1:
    answer = answer1
elif choice == 2:
    answer = answer2
else:
    answer = answer3

print(answer)
