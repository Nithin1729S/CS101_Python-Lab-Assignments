lst=[(1,2,3,1,2,3),(1,2,3,4,7,1),(12,4),(1,2,3,1,2)]
# new_lst=[tuple(set(t)) for t in lst]


def count_duplicates(t):
    for i in range(len(t)):
        return len(t)-len(set(t))


lst.sort(key=count_duplicates)
print(lst)



