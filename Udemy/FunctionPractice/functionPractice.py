def myfunc(word):
    newlist = []
    for n in range(len(word)):
        if (n % 2 == 0):
            newlist.append(word[n].upper())
        else:
            newlist.append(word[n].lower())
    return ''.join(newlist)

myfunc('abcdefghijklmnopqrstuvwxyz')



