'''
the following program is a solution to Challenge 17 in
the programming workbook - Introduction to Programming
in Python
'''

total_amount = 10000
after_tip = 1.15 * total_amount
per_person = after_tip/2
print("each person would pay: ", per_person, " rupees")


# Harder
total_amount = float(input("What is the total bill?\n"))
number_of_people = float(input("How many people are there?\n"))
percentage_tip = float(input("What percentage should the tip be?\n"))
after_tip = (1 + percentage_tip) * total_amount
per_person = after_tip/number_of_people
print("each person would pay: ", per_person_rupees)
