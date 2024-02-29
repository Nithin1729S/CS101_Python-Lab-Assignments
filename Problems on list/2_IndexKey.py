
list_1=[5,1,2,5,4,6,3,5,6,8,4,3,1,5]
index_input=7

key=int(list_1[index_input])
print(key)
# for i in range(len(list_1)):
#     if list_1[i]==key:
#         if i<index:
#             list_1[i]=key-1
#         if i>index:
#             list_1[i]=key+1
#         if i==index:
#             continue
#
#
#
# print(list_1)
#
#

for index,num in enumerate(list_1):
    if num==key:
        if index<index_input:
            list_1[index]=key-1
        if index>index_input:
            list_1[index]=key+1
        if index==index_input:
            continue

print(list_1)
