lower=100
upper=500
list_1=[]
for i in range(lower,upper+1):
    if i%11==0 and i%2!=0:
        list_1.append(i)

print(f"The list of number which are divisible by 11 but not by 2 between {lower} and {upper} are {list_1}")