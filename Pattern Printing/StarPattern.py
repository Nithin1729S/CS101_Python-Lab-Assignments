print("===============================Left Sided Right Triangle==========================================================================")
for i in range(6):
    for j in range(i):
        print("*",end="")
    print()

print("================================Inverse of the same=========================================================================")

for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print()

print("==================================Right Sided Right Triangle=======================================================================")

for i in range(1,6):
    for k in range(1,6-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()

print("===================================Inverse of the same======================================================================")

for i in range(5,0,-1):
    for k in range(1,6-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()
print("=======================================Pyramid==================================================================")

for i in range(1,6):
    for k in range(1,6-i):
        print(" ",end="")
    for j in range(1,(2*i-1)+1):
        print("*",end="")
    print()
print("=======================================Inverse Pyramid==================================================================")

for i in range(5,0,-1):
    for k in range(1,6-i):
        print(" ",end="")
    for j in range(1,(2*i-1)+1):
        print("*",end="")
    print()

print("============================================2 Pyramid Joined together=============================================================")

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

print("=========================================HOurglass================================================================")

for i in  range(5,0,-1):
    for k in range(1,6-i):
        print(" ",end="")
    for j in range(1,(2*i-1)+1):
        print("*",end="")
    print()
for i in  range(2,6):   #decrease one
    for k in range(1,6-i):
        print(" ",end="")
    for j in range(1,(2*i-1)+1):
        print("*",end="")
    print()

print("================================================Left Sided Pyramid==========================================================================")

for i in range(1,6-1):
    for j in range(1,i+1):
        print("*",end="")
    print()
for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print()

print("================================================Right Sided Pyramid==========================================================================")

for i in range(1,6-1):
    for k in range(1,6-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()
for i in range(5,0,-1):
    for k in range(1,6-i):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()
print("================================================Right Sided Pyramid==========================================================================")
