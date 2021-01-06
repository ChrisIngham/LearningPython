# Functions and Methods Homework -- Udemy Bootcamp

# Write a function that computes the volume of a sphere given its radius.
import math
def vol(rad):
    return((4/3) * (math.pi) * (rad**3) )


# Write a function that checks whether a number is in a given range (inclusive of high and low)
def rain_check(num, low, high):
    if (num >= low and num <= high):
        return ("{} is inside the range of {} to {}".format(num, low, high))
    else:
        return (False)

# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
def up_low(s):
    lower_counter = 0
    upper_counter = 0
    for i in range(len(s)):
        if s[i].islower():
            lower_counter +=1
        elif s[i].isupper():
            upper_counter +=1
        else:
            pass
    return ("Original String: {} \n\nExpected Output: \nNumber of UpperCase Characters: {} \nNumber of LowerCase Characters: {}".format(s, lower_counter, upper_counter))

# Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_list(li):
    new_list = []
    for i in range(len(li)):
        if li[i] not in new_list:
            new_list.append(li[i])
    return (new_list)

# Write a Python function to multiply all the numbers in a list.
def multiply(nums):
    total = 1
    for i in range(len(nums)):
        total = total * nums[i]
    return (total)


# Write a Python function that checks whether a word or phrase is palindrome or not.
def palindrome(s):
    new_list = []
    for i in range(len(s)):
        new_list.append(s[i])
    # if I used .reverse() I alter the main list, doing this keeps it original and compares the two
    opposite_list = new_list[::-1]
    if (new_list == opposite_list):
        return(True)
    else:
        return(False)

# Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
import string
def ispangram(str1, alphabet=string.ascii_lowercase):
    counter = 0
    for i in range(len(alphabet)):
        if (str1.count(alphabet[i]) > 0):
            counter += 1
        else:
            break
    if (counter == 26):
        return(True)
    else:
        return(False)

