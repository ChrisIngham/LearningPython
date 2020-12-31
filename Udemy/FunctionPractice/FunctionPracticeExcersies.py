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
    newlist = []
    for i in ran
