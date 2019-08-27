'''
the following program is a solution to Challenge 29 in 
the programming workbook - Introduction to Programming 
in Python 
'''

sentence=input("please enter your sentence\n")
numberE = 0

for letter in sentence:
    if letter == "e":
        numberE += 1

print("The number of e's in the sentence is:", numberE)


## extension

sentence=input("please enter your sentence\n")
number_vowel = 0

for letter in sentence:
    if letter in ("a", "A", "e", "E", "i", "I", "o", "O", "u", "U"):
        number_vowel += 1

print("The number of e's in the sentence is:", number_vowel)
