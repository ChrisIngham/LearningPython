from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def player_guess():
    guess = ''

    while guess not in ['0', '1', '2']:
        guess  = input("Pick a number: 0, 1 or 2: ")

    return int(guess)

def check_guess(mylist, guess):
    if mylist[guess] == 'o':
        print("Correct")
    else:
        print("Wrong Choice")
        print(mylist)

# Inital list
mylist = [' ', 'o', ' ']
# Shuffle list
mix_list = shuffle_list(mylist)
# User guesses
guess = player_guess()
# Check Guess
check_guess(mix_list, guess)