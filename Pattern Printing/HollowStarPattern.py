for i in range(5):
    for j in range(5):
        if j==0 or j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("======================================================================================")
for i in range(5):
    for j in range(5):
        if (j==5//2 or i==5//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("=====================================================================================================================")
for i in range(5):
    for j in range(5):
        if (j==i or i+j==5-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("=====================================================================================================================")


for i in range(5):
    for j in range(5):
        if (j==0 or i==0 or i==5-1 or j==5-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("=============================Hollow Right Sided Right Triangle========================================================================================")

for i in range(1,6):
    for j in range(1,i+1):
        if(j==i or i==5 or j==1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("=====================================================================================================================")

for i in range(5,0,-1):
    for j in range(1,i+1):
        if j==i or i==5 or j==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("=====================================================================================================================")
for i in range(1,6-1):
    for k in range(1,6-i):
        print(" ",end="")
    for j in range(1,(2*i-1)+1):
        print("*",end='')
    print()
for i in range(5,0,-1):
    for k in range(1,6-i):
        print(" ",end='')
    for j in range(1,(2*i-1)+1):
        print("*",end="")
    print()

