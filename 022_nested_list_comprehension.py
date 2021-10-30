ben_matrix = []
for i in range(3):
    #append an empty list
    ben_matrix.append([])

    #populate the empty list
    for j in range(6):
        ben_matrix[i].append(j)

print(ben_matrix)

#another version using nested list comprehension
steve_matrix = [[j for j in range(6)] for i in range(3)]
print(steve_matrix)
