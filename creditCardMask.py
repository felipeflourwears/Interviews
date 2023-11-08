""" Usually when you buy something, you're asked whether your credit card number, 
phone number or answer to your most secret question is still correct. 
However, since someone could look over your shoulder, you don't want that shown on your screen. 
Instead, we mask it.

Your task is to write a function maskify, which changes all but 
the last four characters into '#'.

Examples (input --> output):
"4556364607935616" --> "############5616"
     "64607935616" -->      "#######5616"
               "1" -->                "1"
                "" -->                 ""

// "What was the name of your first pet?"
"Skippy" --> "##ippy"
"Nananananananananananananananana Batman!" --> "################################## """


def creditmask(card):
    print("CARD: ",card)
    digits = ""
    new_card = ""
    if len(card)>4:
        for i in range(0, len(card)-4):
            digits+=card[i]
        for i in range (0, len(digits)):
            new_card+= "#"
        new_card = new_card + card[-4:]
        return new_card
    else:
        return card
print("MASKCARD: ",creditmask("4556364607935616"))
print("MASKCARD: ",creditmask("1"))
print("MASKCARD: ",creditmask("64607935616"))
print("MASKCARD: ",creditmask(""))
print("MASKCARD: ",creditmask("SF$SDfgsd2eA"))


def maskify(cc):
    return "#"*(len(cc)-4) + cc[-4:]

print("MASKCARD: ",maskify("4556364607935616"))
print("MASKCARD: ",maskify("1"))
print("MASKCARD: ",maskify("64607935616"))
print("MASKCARD: ",maskify(""))
print("MASKCARD: ",maskify("SF$SDmaskify"))