#! python3
# mclip.py  - A multi-clipbaord program
""" To get this script to work create a batch file
    put :   @py.exe C:\path_to_file\mclip.py %*
            @pause

    Then in whatever command line, do mclip.bat 'keyphrase'
"""
import sys,pyperclip


TEXT = {
    'agree': """ Yes, I agree. That sounds fine to me. """,
    'busy': """ Sorry, can we do this later this week or next week? """,
    'upsell': """ Would you consider making this a monthly donation? """
}

if len(sys.argv) < 2:
    print("Usage: python mclip.py [keyphrase] - copy phrase text")
    sys.exit()

# reads the first argument passed in the cmd line
keyphrase = sys.argv[1] ## first argument is the keyphrase

# if the text dict contains the keyphrase copy the value to clipboard else, says it is not contained.
if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('text for ' + keyphrase + ' has been copied')
else:
    print('there is no text for ' + keyphrase)

