# define the matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rows=int(len(matrix))
cols=int(len(matrix[0]))


transpose = []

# iterate over the rows of the matrix
for i in range(rows):
    transpose.append([])
    for j in range(cols):
        transpose[i].append(matrix[j][i])

# print the transpose matrix
for row in transpose:
    print(row)
