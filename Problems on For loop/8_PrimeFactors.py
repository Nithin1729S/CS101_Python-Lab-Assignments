num=int(input("Enter a number: "))

for i in range(2,num+1):
    if  num%i==0:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)



