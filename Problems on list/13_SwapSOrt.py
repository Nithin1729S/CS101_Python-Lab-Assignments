a=[3,4,5,2,4,5]

for i in range(len(a)):
    for j in range(len(a) - 1):
        if a[j] > a[j+1]:
            a[j+1], a[j] = a[j], a[j+1]

print(a)