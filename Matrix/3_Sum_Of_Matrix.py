rows = int(input("Enter the number of rows: "))
columns= int(input("Enter the number of columns: "))
matrix=[]
print(f"Enter {rows*columns} entries row wise and press enter after each entry!!!")

for i in range(rows):
    temp=[]
    for j in range(columns):
        temp.append(int(input()))
    matrix.append(temp)

for i in range(rows):
    print(f"Sum of element in row {i+1} = {sum(matrix[i])}")
