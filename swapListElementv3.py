def swapList(newList):
    tupleget = newList[-1], newList[0]
    newList[0], newList[-1] = tupleget

    return newList

whateverList = [10, 11, 14, 9, 12, 5, 20]
print("before swap v3")
print(whateverList)
print("after swap v3")
print(swapList(whateverList))
print("new values of list")
print(whateverList)

