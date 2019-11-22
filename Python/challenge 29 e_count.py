

sentence = input("Please type any sentence and I will calculate the number of letter e's in it.")
numberE = 0

for letter in sentence:
    print(letter)
    if letter =="e":
        numberE +=1
print ("The number of e's in the sentence is:", numberE)
