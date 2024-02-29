string1='pwsroeriusfk'
string2='osu'
#
# indexes=[]
# count=-1
# for i in string1:
#     count+=1
#     if i in string2:
#         indexes.append(count)
#
# print(indexes)

indexes=[]
for i,j in enumerate(string1):
    if j in string2:
        indexes.append(i)

print(indexes)

letters=[]
for i in indexes:
    for j in indexes:


        letters.append(string1[i:j+1])

print(letters)

another_lst=[]
for letter in letters:
    if all(chars in letter for chars in string2):
        another_lst.append(letter)

print(another_lst)

# another_lst.sort(key=len)
#
# print(another_lst[0])
print(sorted(another_lst,key=len))

