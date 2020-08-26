""" 
Returns true is the board param is valid, being passed
    - each board can only have one black and one white king
    - each player must have at most 16 pieces
    - at most 18 pawns
    - cannot go outside of the boards (grid)
    - name must start with w or b (white or black)
        - followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'

"""

def isValidChessBoard(board):
    if (board 


board = {'1h': 'bking', '6c' : 'wqueen', '2g' : 'bbishop', '5h' : 'bqueen', '3e' : 'wking'}
isValidChessBoard(board)