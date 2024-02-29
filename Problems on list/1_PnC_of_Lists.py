string_1=input("Enter the element of the first list seperated by spaces:\n")
string_2=input("Enter the element of the second list seperated by spaces:\n")


list_1=string_1.split()
list_2=string_2.split()
list_3= []

for i in range(len(list_1)):
    for j in range(len(list_2)):
        list_3.append((list_1[i], list_2[j]))

print(list_3)

