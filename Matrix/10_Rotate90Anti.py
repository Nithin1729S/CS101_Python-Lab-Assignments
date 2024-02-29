# def rotate_matrix_anti_clockwise(matrix):
#     """
#     Rotate a matrix 90 degrees anti-clockwise.
#     """
#     n = len(matrix)
#     for i in range(n // 2):
#         for j in range(i, n - i - 1):
#             temp = matrix[i][j]
#             matrix[i][j] = matrix[j][n - i - 1]
#             matrix[j][n - i - 1] = matrix[n - i - 1][n - j - 1]
#             matrix[n - i - 1][n - j - 1] = matrix[n - j - 1][i]
#             matrix[n - j - 1][i] = temp
#
#     return matrix
#

rows=int(input("Enter the number of rows: "))
cols=int(input("Enter the number of columns: "))
matrix=[]
print(f"Enter {rows*cols} elements of the matrix row wise ..Press Enter after each element: ")
for i in range(rows):
    a=[]
    for j in range(cols):
        a.append(int(input()))
    matrix.append(a)

print("The entered matrix is: ")
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j],end=" ")
    print()


for i in range(rows//2):
    for j in range(rows-i-1):
        temp=matrix[i][j]
        matrix[i][j]=matrix[j][rows-i-1]
        matrix[j][rows-i-1]=matrix[rows-i-1][rows-j-1]
        matrix[rows - i - 1][rows - j - 1]=matrix[rows-j-1][i]
        matrix[rows - j - 1][i]=temp

print("The Matrix after rotating it anticlockwise by 90 degrees: ")
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j],end=" ")
    print()














