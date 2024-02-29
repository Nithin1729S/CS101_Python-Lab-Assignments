string_1="abc ab cd efg hij lmn op q"
# string_1=input("Enter the element of the list seperated by spaces:\n")
# letter=input("Enter the letter:\n")
letter='e'
list_1=string_1.split()
a=0
for i in list_1:
    for j in i:
        if j==letter:
            a=list_1.index(i)
            break

else:
    print(a)
