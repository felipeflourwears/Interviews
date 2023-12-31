""" In this kata you are required to, given a string, 
replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string ) """

import string

cadena="The sunset sets at twelve o' clock."

alfabeto = string.ascii_lowercase

def alphabet_position(text):
    dictionary = {}
    for i, letra in enumerate(alfabeto):
        dictionary[letra]= i + 1
    #print(dictionary)
    
    result = ''
    
    for j in text:
        j = j.lower()
        if j in dictionary:
            result = result  + str(dictionary[j])+  " "

    return result[:-1]



print(alphabet_position(cadena))
