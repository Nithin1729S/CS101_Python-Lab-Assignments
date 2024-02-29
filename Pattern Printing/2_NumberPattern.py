rows=5
for i in range(1,rows+1):
    for j in range(i):
        print(i,end=" ")
    print()
print("=============================================================")
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print("=============================================================")
for i in range(rows,0,-1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
print("===============================================================")
b=0
for i in range(rows,0,-1):
    b+=1
    for j in range(1,i+1):
        print(b,end=" ")
    print()
print("==============================================================")
for i in range(rows,0,-1):
    b=5
    for j in range(1,i+1):
        print(b,end=" ")
    print()
print("==============================================================")

i=1
while i<=rows:
    j=1
    while j<=i:
        print((2*i-1),end=" ")
        j+=1
    i+=1
    print()
print("==============================================================")

k=1
for i in range(1,rows+1):
    for a in range(1,rows-i+1):
        print(" ",end="")
    for j in range(0,i):
        if j==0 or i==0:
            k=1
        else:
            k=k*(i-j)//j
        print(k,end=" ")
    print()


