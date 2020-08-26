spam = {'color' : 'blue', 'height' : '6ft', 'age': 42}

# 'indexing'
print ("values: ")
for i in spam.values():
    print(i, end=' ')
print ("\nkeys: ")
for i in spam.keys():
    print(i, end=' ')
    print()
for i,j in spam.items():
    print('Key: ' + i + ', Item: ' + str(j))

print('name' in spam.keys())
print('does name exist? (if not return 0):  \n' + str(spam.get('name', 0)))

# set default, if this value does not exist in dict it will be added.
spam.setdefault('david', 'present')

# using set default to count the frequency of characters with dict.
import pprint 

count ={} 
message = 'count the frequency of the characters in this message'
for char in message:
    count.setdefault(char, 0)
    count[char] = count[char] + 1
pprint.pprint(count)

# Nested Dictonaries
guests = { 'Dave' : { 'apples' : 5, 'pretzels' : 12},
        'Bob' : {'sandwiches' : 3, 'apples' : 2},
        'Carol' : {'cups' : 3, 'pies' : 1}
}
# counts all guest items, and tallies them up. Returns total.
def totalBrought(guests, item):
    numBrought = 0 
    for k,v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print ('Number of things brought: ')
print (' -> Apples      ' + str(totalBrought(guests, 'apples')))
print (' -> Pretzels    ' + str(totalBrought(guests, 'pretzels')))
print (' -> Sandwiches  ' + str(totalBrought(guests, 'sandwiches')))
print (' -> Cups        ' + str(totalBrought(guests, 'cups')))
print (' -> Pies        ' + str(totalBrought(guests, 'pies')))