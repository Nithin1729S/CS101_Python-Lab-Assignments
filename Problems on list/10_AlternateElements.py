string_1=input("Enter the element of the list seperated by spaces:\n")
list_1=string_1.split()
lst=[]

for i in range(0,len(list_1),2):
    lst.append(list_1[i])
print(lst)