import random, sys

print ('Welcome to Rock Paper Scissors')


while True:
    print ('please enter rock paper scissors')
    message = input()

    if (message == 'q'):
        sys.exit()
    elif (message != 'rock' and message != 'scissors' and message != 'paper'):
        continue
    else:
        break

if (message == 'rock'):
    print('Rock is picked by player ')
    user = 1
elif (message == 'paper'):
    print('Paper is picked by player ')
    user = 2
elif (message == 'scissors'):
    print('Scissors is picked by player ')
    user = 3

randomNum = random.randint(1,3)

if (randomNum == 1):
    print('Rock picked by computer ')
    computer = 'rock'
elif (randomNum == 2):
    print('Paper picked by computer')
    computer = 'paper'
elif (randomNum == 3):
    print('Scissors picked by computer')
    computer = 'scissors'
# rock > scissors, scissors > paper, paper > rock
if (user == randomNum):
    print('Resulting in a Tie')
elif ((message == 'rock' and computer == 'scissors' ) or (message == 'scissors' and computer == 'paper') or (message == 'paper' and computer == 'rock') ):
    print('The player has won!')
elif ((computer == 'rock' and message == 'scissors' ) or (computer == 'scissors' and message == 'paper') or (computer == 'paper' and message == 'rock') ):
    print('The computer has won!')
