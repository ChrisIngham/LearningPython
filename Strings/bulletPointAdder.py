#! python3
# adds wiki bullet points to start of each line.
""" Simply create a bat with this inside.
    @py.exe C:\<filepath>\bulletPointAdder.py %*
    @pause
"""
import pyperclip
text = pyperclip.paste()

# Seperate lines and add stars.
lines = text.split('\n')
# for all indexes in 'lines' list
for i in range(len(lines)):
    # add a star at the start of each of these elements
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)

# final, copy back to the clipboard as new text
pyperclip.copy(text)