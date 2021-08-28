def swapList (newList):
    start, *middle, end = newList
    newList = [end, *middle, start]
#    newList[0] = end
#    newList[-1] = start

    return newList

whateverList = [10, 11, 14, 9, 12, 5, 20]
print("before swap v4")
print(whateverList)
print("after swap v4")
print(swapList(whateverList))
print("new values of list")
print(whateverList)