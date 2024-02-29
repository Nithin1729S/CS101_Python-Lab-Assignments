matrix=[[7,1,3,5,3,6],[2,3,6,1,1,6],[5,5,6,1,5,4],[3,5,6,2,7,1],[4,1,4,3,6,4],[4,6,1,7,4,3]]

matrix=[set(i) for i in matrix]
u = list(set.intersection(*matrix))

print(f"The common elements are {u} ")

