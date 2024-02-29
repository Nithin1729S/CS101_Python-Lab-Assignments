import itertools
n=int(input("Enter the number of list: "))
k=int(input("Enter the sum: "))

lst=[]
for _ in range(n):
    temp=list(map(int,input(f"Enter the elements of the {_+1} list seperated with spaces: ").split()))
    lst.append(temp)

output=list(itertools.product(*lst))

l=[]
for _  in output:
    if sum(_)==k:
        l.append(_)
print(l)



