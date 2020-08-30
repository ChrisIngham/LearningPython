# Takes a regular english word and changes it into pig latin
print("Enter the english message you would like translated to pig latin")
text = input()
VOWELS = ('a', 'e', 'i', 'o', 'i', 'y')

pigLatin = []   # List of words in pig lat
for word in text.split():   # seperate non-letters bat start of this word, so we are not left with .oy -> ay.oy
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]     # saves these nonletters in prefixNonLetters
        word = word[1:]     #sets word to everything but first value

    if len(word) == 0 :
        pigLatin.append(prefixNonLetters)
        continue

    suffixNonLetters = ''
    while not word[-1].isalpha():   #seperate the non-letters at the end of this word, so we are not left with oy. -> oy.yay
        suffixNonLetters += word[-1]    #saves these values at the end of the word to suffixNonletters
        word = word[:-1]    #sets word to everything but the last value

    # need to remember the case, before we change to lowercase for translation
    wasUpper = word.isupper()
    wasTitle = word.istitle()
    word = word.lower()

    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:   # seperate the consonants at the start of this word, this will continue from the start until it hits a vowel
        prefixConsonants += word[0]     # adds the consonants to this prefix to be added back
        word = word[1:]     # sets word = word - value in index 0

    # add pig latin to end of word
    if prefixConsonants != '':  # if something is inside prefixConsonants add it followed by ay
        word += prefixConsonants + 'ay'
    else:       # else just add yay to end
        word += 'yay'

    # set back to proper casing
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    # add the non-letters back to the start/end of word, so we have correct punctuation that we started with.
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

# join all as a string and return
print(' '.join(pigLatin))