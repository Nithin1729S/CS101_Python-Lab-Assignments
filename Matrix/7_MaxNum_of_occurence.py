matrix=[[1,2,3,9,9,8],[4,5,6,8,9,9],[7,8,9,9,9,9]]
number=9

rows=len(matrix)
columns=len(matrix[0])

lst=[matrix[i].count(number) for i in range(rows)]
max=lst.index(max(lst))

print(f"The maximum number of {number} is present in {max+1}th row")



