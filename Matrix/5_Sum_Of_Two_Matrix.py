X = [[1,2,3],
    [4 ,5,6]]
 
Y = [[9,8,7],
    [6,5,4]]

result = [[X[i][j] + Y[i][j]  for j in range
(len(X[0]))] for i in range(len(X))]

#
# for i in range(len(X)):
#     temp=[]
#     for j in range(len(X)[0]):
#         temp.append([X[i][j] + Y[i][j])


for i in range(len(X)):
    for j in range(len(X[0])):
        print(result[i][j],end=" ")
    print()
