rows=5
for i in range(1,rows+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
print("====================================================================================================================")

k = 2 * rows - 2  # It is used for number of spaces
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 2   # decrement k value after each iteration
    for j in range(0, i + 1):
        print("* ", end="")  # printing star
    print("")

print("====================================================================================================================")
k = (2 * rows) - 2
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 1  # decrementing k after each loop
    for j in range(0, i + 1):
        # printing full Triangle pyramid using stars
        print("* ", end=' ')
    print(" ")

print("====================================================================================================================")

k=(2*rows)-2
for i in  range(rows,-1,-1):
    for j in range(0,k):
        print(end=" ")
    k+=1
    for j in range(0,i+1):
        print("*",end=" ")
    print()

print("====================================================================================================================")

# It is used to print the space
k = 2 * rows - 2
# Outer loop to print number of rows
for i in range(0, rows):
    # Inner loop is used to print number of space
    for j in range(0, k):
        print(end=" ")
        # Decrement in k after each iteration
    k = k - 1
    # This inner loop is used to print stars
    for j in range(0, i + 1):
        print("* ", end="")
    print("")

# Downward triangle Pyramid
# It is used to print the space
k = rows - 2
# Output for downward triangle pyramid
for i in range(rows, -1, -1):
    # inner loop will print the spaces
    for j in range(k, 0, -1):
        print(end=" ")
        # Increment in k after each iteration
    k = k + 1
    # This inner loop will print number of stars
    for j in range(0, i + 1):
        print("* ", end="")
    print("")

