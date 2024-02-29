lower=int(input("Enter the lower range: "))
upper=int(input("Enter the upper range: "))
even=0
odd=0
for i in range(lower,upper+1):
    if i%2==0:
        even+=1
    else:
        odd+=1

print(f"The number of even numbers in the given range is {even}")
print(f"The number of odd numbers in the given range is {odd}")
