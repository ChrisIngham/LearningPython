# RANDOM LIST FUNCTIONS

idk = [1,2,3,4,5,100,500,10,2]
words = ['i', 'am', 'not', 'creative']
multiList = [['davids','tea'], ['is' , 'alright']]


print(idk[-2])
print(words[int(3.5)])
print(multiList[0][1])


if ('creative' in words):
    print('creative is in words')
else: 
    print('creative is not in words')


cat = ['fat', 'gray', 'loud']
size, colour, demeanor = cat
print('the cat is ' + size + ' and a light shade of ' + colour + ' but is very ' + demeanor)

prac = ['one','small', 'step', 'for', 'man']
print(prac.index('small') )

#immutable
prac.append('kind')
prac.insert(4, 'all')
prac.remove('man')
prac.reverse()
print(prac)
idk.sort(reverse=True)
print(idk)

name = 'zophie a cat'
newName = name[0:7] + 'the' + name[8:]
print('old name ' + name)
print('new name ' + newName)

print(tuple(['cat','dog', 'fish']))
print(list('hello'))
