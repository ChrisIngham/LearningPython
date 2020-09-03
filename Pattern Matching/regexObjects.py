import re
# reg object that contains values seperated by dashes
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# searches the string that we have entered to see if it contains what re.compile's format states.
mo = phoneNumRegex.search('My number is 416-967-1111.')
# mo.group() returns the match we found in mo
print('Phone number found: ' + mo.group())

