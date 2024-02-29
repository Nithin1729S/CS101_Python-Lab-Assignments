lower=int(input("Enter the lower limit: "))
upper=int(input("Enter the upper limit: "))
composite=[]
prime=[]
for num in range(lower,upper+1):
    if num<1:
        raise ValueError("Negative nubmers are not accepted.")
    if num==1:
        continue
    if num>1:
        for i in range(2,num):
            if num%i==0:
                composite.append(num)  #collects all non prime number
                break
        else:#else clause executed  after exhausation of the for loop
            prime.append(num) #collects all prime numbers

print(f"The list of all prime numbers in the given range: {prime}")
print(f"The list of all composite numbers in the given range: {composite}")

