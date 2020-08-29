#only contains nums/letters
while True:
    print('select a new password (letters and nums only)')
    pswd = input()
    if pswd.isalnum():
        break
    else:
        print('passwords can only have numbers & letters')

# creates a partition before and after indicated value
foo = 'hello world'
print(foo.partition('w'))

hell, ow, world = foo.partition('o w')
print (hell + ow + world)

# rjust | ljust | center -- adds characters to right/left or to both sides.
print('right'.rjust(20, '-'))
print('left'.ljust(20, '#'))
print('center'.center(20, '='))
# rstrip | lstrip | strip -- do the opposite and remove the white spaces

