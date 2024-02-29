rows=int(input("Enter the number of rows: "))
cols=int(input("Enter the number of columns: "))
print(f"Enter the {rows*cols} elements of the matrix row wise: ")
mat=[]
for i in range(rows):
    a=[]
    for j in range(cols):
        a.append(int(input()))
    mat.append(a)

for i in range(rows):
    for j in range(cols):
        print(mat[i][j],end=" ")
    print()

sum=0
for i in range(rows):
    for j in range(cols):
        if i==j:
            sum+=mat[i][j]
print(f"Sum of elements of principal diagnol is {sum}")


