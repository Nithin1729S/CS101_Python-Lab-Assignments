def sumoftuple(t):
    return sum(t)

def sort(list):
    tuple_list=[t for t in list if isinstance(t,tuple)]
    other_list=[t for t in list if not isinstance(t,tuple)]
    sorted_list=sorted(tuple_list,key=sumoftuple)+sorted(other_list)
    return sorted_list

print(sort([(1,2,3),(20,),(4,5,6),(45,6),[1,2]]))