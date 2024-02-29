lower=int(input("Enter the lower range: "))
upper=int(input("Enter the upper range: "))
list_1=[]

# for num in range(lower,upper+1):
for num in range(lower,upper+1):
    sum=0
    for i in range(1,num):
            if num%i==0:
                sum+=i

    if sum==num:
            list_1.append(num)

print(list_1)
