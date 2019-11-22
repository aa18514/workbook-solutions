

sentence = input("Please type any sentence and I will calculate the number of vowels in it.")
numberVowels = 0

for letter in sentence:
    print(letter)
    if letter in ('a', 'e', 'i', 'o', 'u'):
        numberVowels +=1
print ("The number of vowelss in the sentence is:", numberVowels)

