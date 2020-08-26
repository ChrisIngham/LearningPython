import time, sys 

# spaces between asterisk
indent = 0

# If you want increasing indentation
indentIncrease = True

try:
    while True: 
        print(' ' * indent, end='')
        print('*****')
        # Pauses for 1/10 of a second so you can see line by line 
        time.sleep(0.1)

        if indentIncrease: 
            indent = indent + 1 
            if indent == 50: 
                # Change directions
                indentIncrease = False
        else: 
            # Changing direction/ decreasing
            indent = indent - 1
            if indent == 0:
                indentIncrease = True
# Continues unless ctrl-c is pressed
except KeyboardInterrupt:
    # Program stops
    sys.exit()