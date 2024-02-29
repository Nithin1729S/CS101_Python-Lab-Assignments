
A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]
 
B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]


rows=int(len(A))
columns=int(len(B[0]))
matrix=[]
for i in range(rows):
    temp=[]
    for j in range(columns):
        temp.append(0)
    matrix.append(temp)
print(matrix)

for i in range(len(A)):
    # iterating by column by B
    for j in range(len(B[0])):
        # iterating by rows of B
        for k in range(len(B)):
            matrix[i][j] += A[i][k] * B[k][j]
print(matrix)

for i in range(rows):
    for j in range(columns):
        print(matrix[i][j], end = " ")
    print()
