num=int(input("Enter a num: "))
# num=123456789
sum=0
while num!=0:
    rem=num%10
    sum+=rem
    num//=10
print(sum)

