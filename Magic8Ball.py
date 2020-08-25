import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2: 
        return 'I am usure'
    elif answerNumber == 3: 
        return 'The result is unceratin'
    elif answerNumber == 4: 
        return 'Outcome will not occur'

r  = random.randint(1,4)
fortune = getAnswer(r)
print(fortune)