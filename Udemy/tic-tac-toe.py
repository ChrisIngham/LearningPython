translation_dict = {
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine"
}

first = second = third = fourth = fifth = sixth = seventh = eighth = ninth = " "

#counter for when it is even its P1 and odd its P2
counter = 0

def translate(location):
    if (counter % 2 == 0):
        value = "X"
    else:
        value = "O"
    # use dict
    translation_dict[location] = value

#def checkspace(location):
    #if (translation_dict[location]) == "X"
    
    
while (True):

    if (counter % 2 == 0):

        location = int(input("\nP1 enter where youd like to put an 'X'\nFrom left to right indicate with a number: "))
        translate(location)
        counter = counter + 1

    else:
        location = int(input("\nP2 enter where youd like to put an 'O'\nFrom left to right indicate with a number: "))
        translate(location)
        counter = counter + 1

    print("{} | {} | {}".format(one, two, three))
    print("---------")
    print("{} | {} | {}".format(four, five, six))
    print("---------")
    print("{} | {} | {}".format(seven, eight, nine))

    #check_for_winner()
