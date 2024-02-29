mat=[[1,2,3],[4,5,6],[7,8,9]]

for i in range(3):
    for j in range(3):
        print(mat[i][j],end=" ")
    print()
    
print(sum(mat[0]))   #returns the sum of elements in a row