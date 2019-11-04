import string


def text_analyzer(txt=""):
    """
    This function counts the number of upper characters,
    lower characters, punctuation and spaces in a given text.
    """
    letters = len(txt)
    uppers = 0
    lowers = 0
    puncts = 0
    spaces = 0
    if not txt:
        print("What is the text to analyse?")
    else:
        for c in txt:
            if (c.isupper()):
                uppers += 1
            elif (c.islower()):
                lowers += 1
            elif (c in string.punctuation):
                puncts += 1
            elif (c.isspace()):
                spaces += 1
        print("The text contains " + str(letters) + " characters")
        print("- " + str(uppers) + " upper letters")
        print("- " + str(lowers) + " lower letters")
        print("- " + str(puncts) + " punctuation marks")
        print("- " + str(spaces) + " spaces")
