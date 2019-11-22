
total_money = input("What is the total amount in Rs. before discount?")
if total_money > 5000:
    discount = 1000
elif total_money > 1000:
    discount = 150
elif total_money > 500:
    discount = 50
elif total_money > 100:
    discount = 5
else:
    disount = 0

discounted_price = total_money - discount

print("The discount you receive is Rs." + str(discount) + " and the discounted price is Rs." + str(discounted_price))



total_money = input("What is the total amount in Rs. before discount?")
if total_money <= 100:
    discount = 0
elif total_money > 100 and total_money <= 500:
    discount = 5
elif total_money > 500 and total_money <= 1000:
    discount = 50
elif total_money > 1000 and total_money <= 5000:
    discount = 150
else:
    disount = 1000

discounted_price = total_money - discount

print("The discount you receive is Rs." + str(discount) + " and the discounted price is Rs." + str(discounted_price))
