import numpy as np

# Displaying Board
def display_board(board):

    print ("{} | {} | {}".format(board[1],board[2],board[3]))
    print ("---------")
    print ("{} | {} | {}".format(board[4],board[5],board[6]))
    print ("---------")
    print ("{} | {} | {}".format(board[7],board[8],board[9]))

# Places X/O in location
def place_marker(position, player):

    board[position] = player

# Checks to see if board is full
def full_board(board):

    count = 0
    for i in board:
        if (i == 'X' or i == "O"):
            count = count + 1
    if count == 9:
        return True
    else:
        return False

# Simple Bool def to ask if user wants to play again
def replay():

    again = input("Would you like to play again? (Yes or No) ")
    while (again != "Yes" and again != "No"):
        again = input("Incorrect Input\nPlease Enter 'Yes' or 'No' if you'd like to play again: ")

    if (again == "Yes"):
        return True
    else:
        return False

# Check if a winner has occured
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

# Before we place something into the board we must make sure nothing is there yet
# Also do checking to make sure value is between 1-9
def check_if_empty(board, pos):
    if (pos >=1 and pos <= 9):
        if (board[pos] == "X" or board[pos] == "O"):
            return False
        else:
            return True
    else:
        return False

# player logic in picking values
player1 = input("Player 1, Choose X or O: ")
while True:
    if (player1 != "X" and player1 != "O"):
        player1 = input("Error, Please enter X or O: ")
    else:
        break
if player1 == "X":
    player2 = "O"
else:
    player2 = "O"

# Meat code

count = 0
board = np.array(['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
display_board(board)

while True:


    if (count % 2 == 0):
        while (True):
            pos = int(input("Player 1 Enter Position (1-9): "))

            if (check_if_empty(board, pos)):
                place_marker(pos, player1)
                count = count + 1
                display_board(board)
                break
            else:
                print("\nThis space is not empty or outside of board\nPlease enter a new position\n")

    else:
        while (True):
            pos = int(input("Player 2 Enter Position (1-9): "))

            if (check_if_empty(board, pos)):
                place_marker(pos, player2)
                count = count + 1
                display_board(board)
                break
            else:
                print("\nThis space is not empty or outside of board\nPlease enter a new position\n")

    # Check for winner
    if (win_check(board, player1)):
        print ("Player 1 has won! ")
        if (replay()):
            indices = [1,2,3,4,5,6,7,8,9]
            board[indices] = " "
            display_board(board)
        else:
            break
    elif (win_check(board, player2)):
        print ("Player 2 has won! ")
        if (replay()):
            indices = [1,2,3,4,5,6,7,8,9]
            board[indices] = " "
            display_board(board)
        else:
            break
    else:
        pass


    # Make sure the board is not full, else we end the game as a tie
    if (full_board(board)):
        print ("Board is Full\nGame has ended in a tie")

        if (replay()):
            indices = [1,2,3,4,5,6,7,8,9]
            board[indices] = " "
            display_board(board)
        else:
            break