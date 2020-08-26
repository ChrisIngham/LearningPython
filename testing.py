birthdays = {'Alice' : 'Apr 1', 'Bob' : 'Dec 12', 'Carol' : 'Mar4'}

while True:
    print ('Enter a name: (Blank to Exit) ')
    name = input()

    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else: 
        print('No information for ' + name) 
        print('Please enter ' + name + "'s birthday: ")
        bday = input()
        birthdays[name] = bday
        print('Our database has been updated... ')

