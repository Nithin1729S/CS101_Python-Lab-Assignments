# string_1=input("Enter the element of the first list seperated by spaces:\n")
# list_1=string_1.split()
list_1=[1,2,3,4,5,6,7,8,9]
for i in range(0,8,2):
    list_1[i],list_1[i+1]=list_1[i+1],list_1[i]

print(list_1)
