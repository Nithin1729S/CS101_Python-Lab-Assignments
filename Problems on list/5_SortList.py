# string_1=input("Enter the element of the list seperated by spaces:\n")
# list_1=string_1.split()
# list_1=[int(i) for i in list_1]
new_list = []

# while list_1:
#     minimum = list_1[0]  # arbitrary number in list
#     for x in list_1:
#         if x < minimum:
#             minimum = x
#     new_list.append(minimum)
#     list_1.remove(minimum)


list_1=[6,4,5,6,8,0,3,4,5,5,6]

for i in range(len(list_1)):
    for j in range(i + 1, len(list_1)):

        if list_1[i] > list_1[j]:
           list_1[i], list_1[j] = list_1[j], list_1[i]

print (list_1)