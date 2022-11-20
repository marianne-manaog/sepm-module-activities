"""
SOURCE OF CODE: https://docs.pylint.org/en/1.6.0/tutorial.html
"""

import string

SHIFT = 3
choice = input("would you like to encode or decode?")
word = (input("Please enter text"))
LETTERS = string.ascii_letters + string.punctuation + string.digits
ENCODED = ''
if choice == "encode":
    for letter_word in word:
        if letter_word == ' ':
            ENCODED = ENCODED + ' '
        else:
            X = LETTERS.index(letter_word) + SHIFT
            ENCODED = ENCODED + LETTERS[X]
        if choice == "decode":
            for letter_word in word:
                if letter_word == ' ':
                    ENCODED = ENCODED + ' '
                else:
                    X = LETTERS.index(letter_word) - SHIFT
                    ENCODED = ENCODED + LETTERS[X]

                print(ENCODED)
