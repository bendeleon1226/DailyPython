x = 1
y = 2
z = 3
n = 4

genList1 = [k for k in range(x+1)]
genList2 = [k for k in range(y+1)]
genList3 = [k for k in range(z+1)]

print(genList1)
print(genList2)
print(genList3)

# list all possible coordinates but sum of coordinates is not equal to n. n value is 4
coordinatesList = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
print(coordinatesList)