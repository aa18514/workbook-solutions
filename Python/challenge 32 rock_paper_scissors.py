import random

score_user = 0
score_computer = 0

name = input('What is your name?')
numRounds = input('How many rounds do you want to play?')

while numRounds < 3 or numRounds > 10:
    numRounds = input('How many rounds do you want to play? Please choose a number between 3 and 10 inclusive')
    

for i in range(numRounds):
    print('Round: ' + str(i+1))
    computer_move = random.randint(1, 3) # 1 is rock, 2 is paper, 3 is scissors
    print('The computer has chosen a move.')
    user_move = input('Please choose your move.Press 1 for rock, 2 for scissors, 3 for paper.')
                                        
    if user_move == 1 and computer_move == 2:    # user chose rock and computer chose paper
        print(name + ' chose rock and the computer chose paper')
        print('The computer won!')
        score_computer+=1

    elif user_move == 1 and computer_move == 3:   # user chose rock and computer chose scissors
        print(name + ' chose rock and the computer chose scissors')
        print(name + ' won!')
        score_user+=1

    elif user_move == 2 and computer_move == 1:  # user chose paper and computer chose rock
        print(name + ' chose paper and the computer chose rock')
        print(name + ' won!')
        score_user+=1
                      
    elif user_move == 2 and computer_move == 3: # user chose paper and computer chose scissors
        print(name + ' chose paper and the computer chose scissors')
        print('The computer won!')
        score_computer+=1

    elif user_move == 3 and computer_move == 1: # user chose scissors and computer chose rock
        print(name + ' chose scissors and the computer chose rock')
        print('The computer won!')
        score_computer+=1
        

    elif user_move == 3 and computer_move == 2: # user chose scissors and computer chose paper
        print(name + ' ''chose scissors and the computer chose paper')
        print(name + ' won!')
        score_user+=1
         

    else: # computer and user move is same
        print("The game is a tie!")
    
print(name + ' has score ' +str(score_user))
print('computer has score ' +str(score_computer))
if score_user > score_computer:
    print(name + ' is the final winner!')
elif score_computer > score_user:
    print('The computer is the final winner')
else:
    print('The game is a draw!')
