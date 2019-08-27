''' 
the following program is a solution to Challenge 46 in 
the programming workbook - Introduction to Programming 
in Python
'''

def littleMonkeys(numMonkeys):
    if type(numMonkeys) != int:    # could have used isinstance(typeMonkeys, int) as well
        return "Please give the number of monkeys jumping on the bed"
    else:
        string = ""
        first_line = " little monkeys jumping on the bed.\n"
        second_line = " One fell down and broke his head.\n"
        third_line = " No more monkeys jumping on the bed.\n"
        for monkey in range(numMonkeys, 0, -1):
            phrase = str(monkey) + first_line + second_line + third_line
            string = string + phrase
    return string

song = littleMonkeys(10)
print(song)


## further extension

def wrong_list_entries(lst):
    invalid_input = False
    for value in lst:
        if type(value) != str:
            invalid_input = True
            break
    return invalid_input


def OldMacDonald(sounds, animals):
    error_message = "Please give to list of strings with equal number of items!"
    if type(sounds) != list or type(animals) != list:
        return error_message
    elif wrong_list_entries(sounds) or wrong_list_entries(animals):
        return error_message
    elif len(sounds) != len(animals):
        return error_message
    else:
        for i in range(len(sounds)):
            print("Old Macdonald had a farm E-I-E-I-O")
            print("And on his farm he had a " + animals[i] + " E-I-E-I-O")
            print("With a " + sounds[i] + "-" + sounds[i] + " here and a " + sounds[i] + \
                    "-" + sounds[i] + " there")
            print("Here a " + sounds[i] + " there a " + sounds[i] +", everywhere a " + \
                    sounds[i] + "-" + sounds[i])

sounds = ['quack', 'woof', 'meow', 'moo', 'neigh', 'baa', 'cluck']
animals = ['duck', 'dog', 'cat', 'cow', 'horse', 'sheep', 'chicken']
OldMacDonald(sounds, animals)


