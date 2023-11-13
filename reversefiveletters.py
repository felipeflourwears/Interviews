"""
Write a function that takes in a string of one or more words, and returns the same string, 
but with all five or more letter words reversed (Just like the name of this Kata). 
Strings passed in will consist of only letters and spaces. 
Spaces will be included only when more than one word is present.

Examples:

spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona test"
"""

def spinWords(text):
    words = text.split()
    new_text = ""

    for word in words:
        if len(word) >= 5:
            new_text += word[::-1] + " "
        else:
            new_text += word + " "

    # Remove the trailing space if there is more than one word or if the input is a single word
    if len(words) > 1 or len(new_text.strip()) == len(text):
        new_text = new_text.rstrip()

    return new_text

text1 = "Welcome"
result1 = spinWords(text1)
print(result1)

text2 = "to"
result2 = spinWords(text2)
print(result2)

text3 = "CodeWars"
result3 = spinWords(text3)
print(result3)

