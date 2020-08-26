import random 

# declare the two counters that will be used to check the streaks
numOfStreaks = 0
streak = 0

for experimentNumber in range(10000):
    flipped = []
    #code that creates the list of 100 'heads' or 'tails' values
    for i in range(100):
        flipped.append(random.randint(0,1))
    
    # code that checks if there is a strek of 6 heads or tails in a row
    for i in range(len(flipped)):
        # checks to see if i == 0 because we must start at index [1] not [0] so will pass back to top
        if i == 0: 
            pass
        # if i - 1 == i, then streak is 1 - then 2 - then 3 - etc...
        elif flipped[i] == flipped[i-1]:
            streak += 1
        # if the i-1 == i is false we must make the streak ==0 
        else:
            streak = 0 
        # once we have a total of 6 streaks we must increment numOfStreaks
        if streak == 6:
            numOfStreaks +=1    
    
print('Chance of streak: %s%%' % (numOfStreaks /(100*10000)))