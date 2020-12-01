import re
# Morse Codes
morse_codes = {"A": ". ___", "B": "___ . . .", "C": "___ . ___ .", "D": "___ . .", "E": ".", "F": ". . ___ .", "G": "___ ___ .", "H": ". . . .", "I": ". .", "J": ". ___ ___ ___", "K": "___ . ___", "L": ". ___ . .", "M": "___ ___", "N": "___ .", "O": "___ ___ ___", "P": ". ___ ___ .", "Q": "___ ___ . ___", "R": ". ___ .", "S": ". . .", "T": "___",
               "U": ". . ___", "V": ". . . ___", "W": ". ___ ___", "X": "___ . . ___", "Y": "___ . ___ ___", "Z": "___ ___ . .", "1": ". ___ ___ ___ ___", "2": ". . ___ ___ ___", "3": ". . . ___ ___ ___", "4": ". . . . ___", "5": ". . . . .", "6": "___ . . . .", "7": "___ ___ . . .", "8": "___ ___ ___ . .", "9": "___ ___ ___ ___ .", "0": "___ ___ ___ ___ ___"}


def Text_MorseCode_Converter(text):
    morse_code = ""

    # remove extra white spaces
    text = re.sub("\s\s+", " ", text)
    # convert to upper case letters
    text = text.upper()
    for letter in text:
        if letter in morse_codes:
            morse_code += (morse_codes[letter]+"   ")
        elif letter == " ":
            morse_code += "    "
        else:
            return "Please make sure there is no illegal input."

    return morse_code.strip()
