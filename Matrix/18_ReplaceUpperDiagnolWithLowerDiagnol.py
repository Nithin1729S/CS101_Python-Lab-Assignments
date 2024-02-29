
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Print the input matrix
print("Input Matrix:")
for i in range(3):
    for j in range(3):
        print(matrix[i][j], end=" ")
    print()

# Swap the upper diagonal elements with the lower diagonal elements
for i in range(3):
    for j in range(i):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# Print the output matrix
print("\nOutput Matrix:")
for i in range(3):
    for j in range(3):
        print(matrix[i][j], end=" ")
    print()



















