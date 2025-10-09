haystack = [-20, -15, -12, -8, -5, -3, 1, 2, 4, 6, 7, 9, 11, 14, 15, 19, 23, 25, 28, 31]

def binsearch(needle, haystack):
    low = 0
    high = len(haystack) - 1

    while low <= high:
        middle = (low + high) // 2

        if haystack[middle] > needle:
            high = middle - 1
        elif haystack[middle] < needle:
            low = middle + 1
        else: # dvs. de är lika
            return middle

    return -1


#### Test the function

for needle in [9, 1, 13]:
    index = binsearch(needle, haystack)
    if index < 0:
        print(f"The value {needle} was not found")
    else:
        print(f"The index for {needle} is: {index}")