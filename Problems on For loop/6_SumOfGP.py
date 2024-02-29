a=int(input("Enter a: "))
n=int(input("Enter n: "))
r=int(input("Enter r: "))
sum=0
for i in range(n+1):
    sum+=a*(r**i)

print(f"The sum of the sequence is {sum}")



