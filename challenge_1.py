'''
the following program is a solution to Challenge 1 in
the programming workbook - Introduction to Programming
in Python
'''


firstName = input("what is your first name?\n") # ask user for his first name
surName = input("what is your surname?\n") # ask user for his surname
print(surName, firstName) # display surname followed by first name

# extension
print(surName, " ", firstName) # how is this result different from the earlier result?


fullName = firstName + surName # place surname after firstName
print (fullName) # what gets printed on the screen?

