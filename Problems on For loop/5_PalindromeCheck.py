num=int(input("Enter a number to check if it is a Palindrome: "))
if str(num)==(str(num)[::-1]):
    print(f"{num} is a Palindrome")
else:
    print(f"{num} is not a Palindrome")

