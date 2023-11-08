""" Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3] """


print("Example Mio")
def array_diff(a1,a2):
    a3=[]
    for i in a1:
      if i not in a2:
        a3.append(i)
    return a3


print(array_diff([1,2],[1]))

print("Example")
def array_diff(array1, array2):
    return [x for x in array1 if x not in array2]

# Ejemplo de uso
resultado = array_diff([1, 2], [1])
print(resultado)  # Salida esperada: [2]