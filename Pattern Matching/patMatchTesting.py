import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 416-967-1111.')
areaCode, mainNumber = mo.groups()

heroRegex = re.compile(r'Batman | Tina Fey')
hero1 = heroRegex.search('Batman and Tina Fey')

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
batMatch = batRegex.search('Batmobile lost a wheel')

print('The area code is: ' + areaCode + ', with the following number: ' + mainNumber)
print('Also my favourite super hero is: ' + hero1.group() + 'especially on his ' + batMatch.group())