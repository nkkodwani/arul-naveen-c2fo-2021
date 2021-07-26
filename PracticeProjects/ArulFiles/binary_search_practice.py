#ELEMENT (Binary) SEARCH: Excercise 20 from practicepython.org

#inp = [1, 2, 3, 4, 5, 5, 7, 8, 9, 9, 10, 12, 15, 17, 17, 18, 19, 21, 25, 26, 28, 28, 30, 32, 33, 34, 35]
inp = [i for i in range(0, 10000000)] 

def binary_search(inp, num): #has O(log n) time
    searched  = False
    inList = False
    out = int()
    while not searched:
        mid_index = int((len(inp) // 2))
        if num == inp[mid_index]:
            inList = True
            searched = True
            out = mid_index
        elif num < inp[mid_index]:
            inp = inp[:mid_index]
        elif num > inp[mid_index]:
            inp = inp[mid_index:]
        else: 
            return "Element is not present in list"
    return inList

print(binary_search(inp, 10000000))


