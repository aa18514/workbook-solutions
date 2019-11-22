import random
friend1_pass = random.getrandbits(1) 
friend2_pass = random.getrandbits(1)
friend3_pass = random.getrandbits(1)
if (friend1_pass and friend2_pass and friend3_pass):
    print("all friends have a pass to enter Aladdin")
elif (friend1_pass or friend2_pass or friend3_pass):
    print("atleast one of the friends has a pass to enter Aladdin")
else:
    print("no one has a pass to enter Aladdin")



### extension

import random
friend1_pass = random.getrandbits(1) 
friend2_pass = random.getrandbits(1)
friend3_pass = random.getrandbits(1)
is_friend1_mischievous = random.getrandbits(1)
if (friend1_pass and friend2_pass and friend3_pass):
    print("all friends have a pass to enter Aladdin")
    if is_friend1_mischievous == True:
        print('Even though she has a pass, the first friend cannot enter because she has been mischevious')
        
elif (friend1_pass or friend2_pass or friend3_pass):
    print("atleast one of the friends has a pass to enter Aladdin")
    
    if (is_friend1_mischievous and friend1_pass):
        print('Even though she has a pass, the first friend cannot enter because she has been mischevious')
else:
    print("no one has a pass to enter Aladdin")


### extension b

import random
friend1_pass = True
friend2_pass = False
friend3_pass = False
is_friend1_mischievous = True
if (friend1_pass and friend2_pass and friend3_pass):
    print("# all friends have a pass to enter Aladdin")
    if is_friend1_mischievous == True:
        print('Even though she has a pass, the first friend cannot enter because she has been mischievous')
        
elif (friend1_pass or friend2_pass or friend3_pass):
    print("atleast one of the friends has a pass to enter Aladdin")
    
    if (is_friend1_mischievous and friend1_pass):
        print('Even though she has a pass, the first friend cannot enter because she has been mischievous')
else:
    print("no one has a pass to enter Aladdin")

