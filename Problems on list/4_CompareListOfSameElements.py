# string_1=input("Enter the element of the first list seperated by spaces:\n")
# string_2=input("Enter the element of the second list seperated by spaces:\n")
# list_1=string_1.split()
# list_2=string_2.split()
list_1=[1,2,3,4]
list_2=[3,4,5,6,7]
# count=0
# for i in list_1:
#     for j in list_2:
#         if i==j:
#             count+=1
# else:
#     print(count)

common=set(list_1)&set(list_2)
print(len(common))


