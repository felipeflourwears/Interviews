"""The goal of this exercise is to convert a string to a new string 
where each character in the new string is "(" if that character appears 
only once in the original string, or ")" 
if that character appears more than once in the original string. 
Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 


Notes
Assertion messages may be unclear about what they display in some languages. 
If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!
"""
cadena = "(( @"
count_letters={}


def func_duplicate(cadena):
    new_cadena=""
    for letra in cadena:
        print(letra)
        letra=letra.lower()
        if letra in count_letters:
            count_letters[letra]+= 1
        else:
            count_letters[letra]=1
    print(count_letters)


    for letra in cadena:
        letra=letra.lower()
        if letra in count_letters:
            count=count_letters[letra]
            print("Letra: ", letra, "Count: ", count)
            if count > 1:
                new_cadena+=")"
                print("...",new_cadena)           
            else: 
                new_cadena+="("
                print("...",new_cadena)   
    return new_cadena

print(func_duplicate(cadena))



















""" cadena="din"
contador_letras={}

def codifier(cadena):
    new_cadena=""
    
    # Count letters into dictionary and store values
    for i in cadena:
        i= i.lower()
        if i in contador_letras:
            contador_letras[i] += 1
        else:
            contador_letras[i] = 1
        print(contador_letras)

    # Show count from dictionary
    for letra, count in contador_letras.items():
        print(f"La letra {letra} se repite: {count}")

    for letra in cadena:
        letra=letra.lower()
        #Verify if letra is in dictionary(contador de letras)
        if letra in contador_letras:
            #Based on the letter, look for its value, the letter is the key
            veces = contador_letras[letra]
            if veces == 1 :
                letra_new=letra.replace(letra, "(")
                new_cadena += letra_new
            else:
                letra_new=letra.replace(letra, ")")
                new_cadena += letra_new
            print("True: ", letra , "Veces: ", veces)
        else:
            print("False: ", letra)


    print("codifier: ", new_cadena)


codifier(cadena) """

