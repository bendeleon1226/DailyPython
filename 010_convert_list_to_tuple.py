list_countries = ["philippines","singapore","USAM","Germany","Malaysia","India","Indonesia","Myanmar"]
print("list_countries elements:", list_countries)
tuple_countries = *list_countries, #take note of the comma and *. this will convert list to tuple
print("tuple_countries:", tuple_countries)

result = zip(*list_countries)
print("result tuple", result)

list1 = list(result)
print("list1 elements:", list1)

lst = [['x', 'y'], ['a', 'b'], ['m', 'n']]
print("lst elements:", lst)
tuple_lst = *lst,
print("tuple_lst:", tuple_lst)

result2 = zip(*lst)
print("result2 tuple", result2)

list2 = list(result2)
print("list2 elements:", list2)



mergedList = []
x = 1
#loop through tuple
for ele in list2:
    print(x)
    print("element in tuple form: ", ele)
    print("element in list form: ", list(ele))
    mergedList.append(list(ele))
    x = x + 1

print("Merged List: ", mergedList)