def christmasSong():
    days = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
    gifts = ['a partridge in a pear tree', 'two turtle doves', 'three French hens', 'four calling birds', 'five gold rings', 'six geese a laying',
             'seven swans a swimming','eight maids a milking', 'nine ladies dancing', 'ten lords a leaping', 'eleven pipers piping', 'twelve drummers drumming']   
    for i in range(len(days)):
        print("On the " + days[i] + " of Christmas my true love sent to me,")
        numGifts = i
        while numGifts >= 0:
            if numGifts == 0 and i != 0:
                print("and " + gifts[numGifts])
            else:
                print(gifts[numGifts])
            numGifts = numGifts - 1
    


def littleMonkeys(numMonkeys):
    if type(numMonkeys) != int:
        return("Please give me the number of monkeys jumping on the bed")
    jumping = "jumping on the bed.\n One fell down and broke his head.\n Mama called the doctor doctor said.\n No more monkeys jumping on the bed"
    while numMonkeys > 1:
        print(str(numMonkeys) + " little monkeys " + jumping)
        numMonkeys = numMonkeys - 1
    print(str(numMonkeys) + " little monkey " + jumping)



def oldMacDonald(sounds, animals):
    #sounds = ['quack', 'woof', 'meow', 'moo', 'neigh', 'baa', 'cluck']
    #animals = ['duck',  'dog', 'cat',  'cow', 'horse', 'sheep', 'chicken']
    eieio = ' E-I-E-I-O'
    
    print('Old MacDonald had a farm ' + eieio)
    for i in range(len(sounds)):
        print('And on his farm he had a ' + animals[i] + eieio)
        print('With a ' + sounds[i] + '-' + sounds[i]  + ' here' + ' and a '+ sounds[i] + '-' + sounds[i] + ' there')
        print('Here a ' + sounds[i] +  ' there a ' + sounds[i] + ', everywhere a ' + sounds[i] + '-' + sounds[i])
        print('Old MacDonald had a farm ' + eieio)
                   
