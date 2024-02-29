num=int(input("Enter the number: "))
sum=0
for digits in str(num):
    sum+=int(digits)



print(f"The sum of all digits of the given number is {sum}")