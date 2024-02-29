
# print(int(n,10))  #10 represents the number system n is curretly in. It is default set to 10.To use second argument of int funtion th efirst one must be a integer
# print(int(n,2))  # thinks 100 is a binary and returns 4
# print(bin(int(n)))
def binary_to_gray(n):
    n=int(n,2)   #We have to make sure n is a string
    n^=(n>>1)
    return bin(n)[2:]

binary_value=input("Enter the binary number: ")
gray_value=binary_to_gray(binary_value)
print(f"The Gray Code of {binary_value} is {gray_value}")


# #The function ‘int()’ converts the binary number to a decimal integer number as follows-
# int(string, base) –> Here, the string is the binary number and the base for a binary number is 2.
# Then, we perform the XOR operation of number with another number obtained by right shifting the number by 1 bit.
# binary ^= (binary >> 1) –> The symbol ‘^’ denotes XOR operation.
# XOR is performed between ‘binary’ and ‘binary >> 1’ where the symbol ‘>>’ denotes the right shift and 1 denotes the right shift by 1 bit.