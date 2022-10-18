# Write a function that returns the intersection of two arrays. The intersection is a third array that contains all values contained within the first two
# arrays. For example, the intersection of [1, 2, 3, 4, 5] and [0, 2, 4, 6, 8] is [2, 4].
# Your function should have a complexity of O(N).
lista = [1,2,3,4,5]
listb = [0, 2, 4, 6, 8]
listc =[]
def intersection(lista, listb):
    hashtable = {}
    for char in lista:
        hashtable[char] = True
    for val in listb:
        if val in hashtable:
            listc.append(val)
    print(listc)
intersection(lista, listb)
