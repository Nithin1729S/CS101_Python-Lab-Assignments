#import itertools
import random
#list2 = [[1,2,3,4,10],[4,5,6,8,87],[9,10,11,12,56],[13,14,15,17,59],[34,67,23,24,43]]
# list2 = [[1,1,2,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]

n = int(input("Enter the number of lists: "))
list2 = []
for i in range(n):
    lst = list(map(int, input(f"Enter the elements of list {i+1} separated by space: ").split()))
    list2.append(lst)

k = int(input("Enter the sum number: "))

# print(list2)
list3 = []
for i in range(1,45000):
    list1 = []
    for j in range(n):
        x = random.randrange(n)
        element = list2[j][x]
        list1.append(element)
    if list1 not in list3:
        list3.append(list1)
    if len(list3) == n**n:
        break
list4 = []



for i in list3:
    sum = 0
    for j in i:
        sum = sum + j
    if sum == k:
        list4.append(i)


print(list4)
#print(len(list3))

#print(len(list(itertools.product(*list2))))


