
def removepair(x, y, lst):
    pair_to_remove = (x, y)
    new_lst=[]
    for i in lst:
        if isinstance(i,tuple):
            if x not in i and y not in i:
                new_lst.append(i)
            else:
                continue
        else:
            new_lst.append(i)
    print(new_lst)

removepair(x= 3, y= 5, lst = [(1, 2), (1), 4, (3, 5, 7), (5, 7, 8, 3, 5), (5, 3, 3), (5, 3, 5), [3, 5]])