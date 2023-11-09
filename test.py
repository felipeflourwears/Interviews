""" Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3] """


def dif(array1, array2):
    arraydif=[]
    for i in array1:
        print(i)
        if i not in array2:
            print("Este numero no esta en array2: ", i)
            arraydif.append(i)
    return arraydif

print(dif([1,2],[1]))


""" 
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

Examples (Input --> Output)
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false 
"""


def valdidate_pin(pin):
    if len(pin)==4 or len(pin)==6:
        if pin.isdigit():
            return True
        else:
            return False
    else:
        return False
    
print(valdidate_pin("a234"))

