"""
Just a simple program that takes any length list and seprates the list and outputs it with 'and' for last value
"""

def foo (li):
    for i in range(len(li)-1):
        print ( li[i] , end='' + ', ')
    print ('and ' + li[-1])

idk = ['welcome', 'to', 'davids', 'tea']
foo(idk)
