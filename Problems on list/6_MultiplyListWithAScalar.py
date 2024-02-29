string_1=input("Enter the element of the first list seperated by spaces:\n")
scalar=int(input("Enter the number to be multiplied with:\n"))
list_1=string_1.split()
for i in range(0,len(list_1)):
    list_1[i]=int(list_1[i])
    list_1[i]=scalar*list_1[i]

print(list_1)



















