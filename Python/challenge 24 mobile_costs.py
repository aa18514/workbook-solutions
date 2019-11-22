pictures = input('How many pictures would you send over text message each month?')
texts = input('How many text messages would you need to send?')
data = input('How much data would you use in MB?')


total = 25 * int(pictures) + 0.5* int(texts) + 10*float(data)
print('Your total bill is Rs.' + str(total))

if total > 100:
    print('Since your total is greater than 100, you are advised to subscribe to some package.')

    
