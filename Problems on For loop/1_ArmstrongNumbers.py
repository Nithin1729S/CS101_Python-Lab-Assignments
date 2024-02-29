lower=int(input("Enter the lower range: "))
upper=int(input("Enter the upper range: "))
list_1=[]
for i in range(lower,upper+1):
    sum=0
    for digits in str(i):
        sum+=(int(digits))**3
    if sum==i:
        list_1.append(sum)

print(f"The list of all armstrong numbers between {lower} and {upper} is {list_1}")