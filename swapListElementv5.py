def swapList(newList):
    first = newList.pop(0)
    last = newList.pop(-1)

    newList.insert(0, last)
    newList.append(first)

    return newList

whateverList = [10, 11, 14, 9, 12, 5, 20]
print("before swap v5")
print(whateverList)
print("after swap v5")
print(swapList(whateverList))
print("new values of list")
print(whateverList)