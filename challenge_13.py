''' 
Challenge 13 - Dividing

Ask user the number of family members in his family.
Split Rs 10,000 evenly between the family members.
Print the amount that each family member should get.
'''

shares = int(input("How many people do you want to share the money with?\n"))
money = 1000/shares
print("each person in the family gets: " + money + " rupees")
