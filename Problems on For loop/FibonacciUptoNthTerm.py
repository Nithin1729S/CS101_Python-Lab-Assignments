num=int(input("Enter a number: "))
f1=0
f2=1
list_1=[0,1]
for i in range(2,num):
    next_term=f1+f2
    f1=f2
    f2=next_term
    list_1.append(next_term)

print(list_1)