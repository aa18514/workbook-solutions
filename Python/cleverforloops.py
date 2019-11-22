sentence = "Here is a sentence. How many letter 'e''s are there in it?"
numberE = 0

for letter in sentence:
    print(letter)
    if letter =="e":
        numberE +=1
print ("The number of e's in the sentence is:", numberE)
