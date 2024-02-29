# def rotate(matrix):
#     n = len(matrix)
#     for i in range(n // 2):
#         for j in range(i, n - i - 1):
#             temp = matrix[i][j]
#             matrix[i][j] = matrix[n - j - 1][i]
#             matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
#             matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
#             matrix[j][n - i - 1] = temp
#     return matrix
#
# print(rotate([[2,3,4],[7,5,6],[3,3,4]]))
#


rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columnsd: "))
matrix = []
print(f"Enter {rows * cols} elements row wise and press enter after each element: ")

for i in range(rows):
    a = []
    for j in range(cols):
        a.append(int(input()))
    matrix.append(a)

print("The entered matrix is: ")
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=" ")
    print()

for i in range(rows // 2):
    for j in range(rows - i - 1):
        temp = matrix[i][j]
        matrix[i][j] = matrix[rows - j - 1][i]
        matrix[rows - j - 1][i] = matrix[rows - i - 1][rows - j - 1]
        matrix[rows - i - 1][rows - j - 1] = matrix[j][rows - i - 1]
        matrix[j][rows - i - 1] = temp

print("The matrix after rotating clockwise by 90 degrees: ")

for i in range(rows):
    for j in range(cols):
        print(matrix[i][j],end=' ')
    print()




