import random

messages = ['It is certain',
    'most likely',
    'unsure',
    'very unlikely',
    'will not occur']

print(messages[random.randint(0,len(messages)-1)])