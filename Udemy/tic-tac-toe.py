# Generate tic-tac-toe board
import random

def display_board(board):

    print ("{} | {} | {}".format(board[1],board[2],board[3]))
    print ("---------")
    print ("{} | {} | {}".format(board[4],board[5],board[6]))
    print ("---------")
    print ("{} | {} | {}".format(board[7],board[8],board[9]))

    pass

# Get users input and know which player is playing at a time
def player_input():

    player_response = input("Player {} Choose 'X' or 'O': ".format(choose_first()) )
    while (player_response != "X" and player_response != "O"):
        player_response = input("Sorry, incorrect input\nPlayer {} Choose 'X' or 'O': ".format(choose_first()))

    return player_response


# Takes board list, 'X' or 'O', and position
def place_marker(board, marker, position):

    board[position] = marker

# Check to see if a player has won, checks to see if a 'X' mark or 'O' mark has won
def win_check(board, mark):
    if (board[1] == mark and board[2] == mark and board[3] == mark):
        return True
    elif (board[1] == mark and board[4] == mark and board[7] == mark):
        return True
    elif (board[2] == mark and board[5] == mark and board[8] == mark):
        return True
    elif (board[3] == mark and board[6] == mark and board[9] == mark):
        return True
    elif (board[4] == mark and board[5] == mark and board[6] == mark):
        return True
    elif (board[7] == mark and board[8] == mark and board[9] == mark):
        return True
    elif (board[3] == mark and board[5] == mark and board[7] == mark):
        return True

# Randomly Chooses which player goes first
def choose_first():
    player = random.randint(0,1)

    if (player == 0):
        return ("1")
    else:
        return ("2")

# Checks to see if a space is empty
def space_check(board, position):

    if (board[position] == 'X' or board[position] == "O"):
        return False
    else:
        return True

# Checks to see if the whole board is full
def full_board_check(board):

    count = 0
    for i in range(9):
        if (board[i] == 'X' or board[i] == "O"):
            count = count + 1
    if count == 9:
        return True
    else:
        return False

# Takes the users choice in position and returns if the space is free in that spot
def player_choice(board):
    position = int(input("Please Choose a Location (1-9): "))

    return (space_check(board, position))

# Ask if the user wants to play again
def replay():
    again = input("Would you like to play again? (Yes or No): ")

    if (again == "Yes"):
        return True
    else:
        return False

# Main Function
print ("Tic Tac Toe")

# Logic for assigning player1 and player2 'x' or 'o'
value = player_input()
first = choose_first()
if (first == "1"):
    player1 = value
    if (value == "X"):
        player2 = "O"
    else:
        player2 = "X"
else:
    player2 = value
    if (value == "X"):
        player1 = "O"
    else:
        player1 = "X"

print ("Player 1 value {} and Player 2 value {}".format(player1, player2))

count = int(first)

while (True):

    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    display_board(board)


    while ((not(win_check(board, 'X'))) and (not(win_check(board, 'O'))) and (not(full_board_check(board)))):


        if (count % 2 == 1):
            # Player 1 logic
            print("Player 1's Turn")
            pos1 = player_choice(board)
            while (True):
                if (space_check(board, pos1)):
                    place_marker(board, player1, pos1)
                    count = count + 1
                    display_board(board)
                    break
                else:
                    pos1 = int(input("\nNot Free\nPlease Enter a Free Space (1-9): "))
        else:
            # Player 2 Logic
            print("Player 2's Turn")
            pos2 = player_choice(board)
            while (True):
                if (space_check(board, pos2)):
                    place_marker(board, player2, pos2)
                    count = count + 1
                    display_board(board)
                    break
                else:
                    pos2 = int(input("\nNot Free\nPlease Enter a Free Space (1-9): "))

    print("Game OVER")
    # After game completed ask if a replay is wanted
    if not replay():
        break