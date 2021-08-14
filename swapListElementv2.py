def swapList(newList):
    # -1 index means last element of the list
    newList[0], newList[-1] = newList[-1], newList[0]

    return newList

whateverList = [10, 11, 14, 9, 12, 5, 20]
print("before swap v2")
print(whateverList)
print("after swap v2")
print(swapList(whateverList))
