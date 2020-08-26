theBoard = {
    'top-L' : ' ', 'top-M' : ' ', 'top-R' : ' ',
    'mid-L' : ' ', 'mid-M' : ' ', 'mid-R' : ' ',
    'bot-L' : ' ', 'bot-M' : ' ', 'bot-R' : ' '
}

def printBoard ():
    print (theBoard['top-L'] + '|' + theBoard['top-M'] + '|' + theBoard['top-R'])
    print ('-+-+-')
    print (theBoard['mid-L'] + '|' + theBoard['mid-M'] + '|' + theBoard['mid-R'])
    print ('-+-+-')
    print (theBoard['bot-L'] + '|' + theBoard['bot-M'] + '|' + theBoard['bot-R'])
printBoard()

turn = 'X'
for i in range(9):
    printBoard()
    print('Turn for ' + turn + ', move on which space? ')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else: 
        turn = 'X'
printBoard()