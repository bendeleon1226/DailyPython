def calcLength(n):
  return len(n)

x = map(calcLength, ('philippines', 'singapore', 'malaysia'))

#print the map object
print(x)

#convert the map into a list for readability
print(list(x))

str = "98 98 98 98 98 98 98 98"
arr = map(int, str.split())
print(arr)
normalList = list(arr)
print(normalList)
normalList.sort()
print(normalList);
print("length: ", end="")
print(len(normalList))
length_of_list = len(normalList)

start = -2;
i = 1
while (i<length_of_list):
    if normalList[-1] == normalList[start]:
        start = start - 1
    else:
        break
    i=i+1

print(i)
if i == length_of_list:
    print("Second highest number is not found")
else:
    print("Second highest number is: ", end="")
    print(normalList[start])
#while()
#print("Second highest: ", end="")
#print(normalList[-2])
