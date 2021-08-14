def swapList(newList):
    size = len(newList)

    #place the first element to temp
    temp = newList[0];

    #let's swap
    newList[0] = newList[size-1]
    newList[size-1] = temp

    return newList

#this is the list
whateverList = [10, 11, 14, 9, 12, 5, 20]
print("before swap")
print(whateverList)
print("after swap")
print(swapList(whateverList))
