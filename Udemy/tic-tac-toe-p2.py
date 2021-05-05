def display_board(board):

    print ("{} | {} | {}".format(board[1],board[2],board[3]))
    print ("---------")
    print ("{} | {} | {}".format(board[4],board[5],board[6]))
    print ("---------")
    print ("{} | {} | {}".format(board[7],board[8],board[9]))

def place_marker(position, player):

    board[position] = player


player1 = 'X'
player2 = 'O'

board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
display_board(board)

count = 0 
while True:
    if (count % 2 == 0):
        pos = int(input("Position: "))
        place_marker(pos, player1)
        display_board(board)
        count = count + 1
    else:
        pos = int(input("Position: "))
        place_marker(pos, player2)
        display_board(board)
        count = count + 1