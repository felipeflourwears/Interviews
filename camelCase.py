"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
The first word within the output should be capitalized only if the original word 
was capitalized (known as Upper Camel Case, also often referred to as Pascal case). 
The next words should be always capitalized.

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"

"""
text = "the-stealth-warrior"
text1 = "The_Stealth-Warrior"
text2 = "The_Stealth-Warrior"
def camel_case(text):
    new_text=""
    mayus = False
    for i in text:
        if i != "-" and i != "_":
            #print("Letra: ", i)
            if mayus == True:
                i=i.upper()
            new_text += i
            mayus = False
        else:
            mayus = True
    return new_text

print(camel_case(text))
print(camel_case(text1))
print(camel_case(text2))

"""Best Practice"""
print("\nBEST PRACTICE:\n")
def to_camel_case(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])

print(camel_case(text))
print(camel_case(text1))
print(camel_case(text2))
