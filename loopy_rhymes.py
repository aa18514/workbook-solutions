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

