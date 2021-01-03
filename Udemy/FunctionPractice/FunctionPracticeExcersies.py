## Questions for the Functions and Methods part of the Udemy course.

# Level 1 Problems
# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(name):
    newlist = []
    for i in range(len(name)):
        if (i == 0) or (i == 3):
            newlist.append(name[i].upper())
        else:
            newlist.append(name[i])
    return (''.join(newlist))

# MASTER YODA: Given a sentence, return a sentence with the words reversed
def master_yoda(sentance):
    newlist = sentance.split()
    newlist.reverse()
    print(' '.join(newlist))

# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200¶
def almost_there(number):
    if ((number >= 90 and number <= 110) or (number >= 190 and number <=110)):
        return True
    else:
        return False


# Level 2 Problems
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def thirty_three(ray):
    for i in range(len(ray)):
        if (ray[i] == 3 and ray[i-1] == 3):
            return("True")
            quit()
        else:
            pass
    return("False")


# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
def paper_doll(doll):
    newlist = []
    for i in range(len(doll)):
        newlist.append((doll[i])*3)

    return(''.join(newlist))

# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
def blackjack(a,b,c):
    total = a+b+c
    if (total <= 21):
        return (total)
    elif (total > 21 and (a == 11 or b == 11 or c == 11)):
        total = total - 10
        return (total)
    else:
        return ("Bust")

# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and
# extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
def summer_of_69(arr):
    total = 0
    index_of_6 = 0
    index_of_9 = 0
    for i in range(len(arr)):
        if (arr[i] == 6):
            index_of_6 = i
        elif (arr[i] == 9):
            index_of_9 = i
        else:
            pass

    if (arr.count(6) > 0):
        for i in range(len(arr)):
            if (i >= index_of_6 and i<= index_of_9):
                pass
            else:
                total = total + arr[i]
    else:
        for i in range(len(arr)):
            total = total + arr[i]

    return(total)


# Challenging Problems
# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(arr):
    if (arr.count(0) > 1) and (arr.count(7) > 0):
        if arr.index(7) > arr.index(0):
            return (True)
        else:
            return (False)
    else:
        print(False)

# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
def count_primes(number):
    # make a variable be the divisior and incremement it until you can divide number with it, until it equals the number value, when it hits that return false
    


