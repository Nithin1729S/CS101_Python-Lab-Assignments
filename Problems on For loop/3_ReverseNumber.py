num=int(input("Enter a number to be reversed: "))
# print(str(num)[::-1])
reverse=0
while num!=0:
    remainder=num%10
    reverse=(reverse*10)+remainder
    num//=10


print(f"The reversed form of the entered number is {reverse}")







