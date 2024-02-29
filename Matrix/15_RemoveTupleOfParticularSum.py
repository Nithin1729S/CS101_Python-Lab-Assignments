def removetup(lst,sm):
    for i in lst:
        if isinstance(i,tuple):
            if sum(i)==sm:
                lst.remove(i)
    return lst

sm=27
lst=[(1,3,5),(27),(3,3,1,20),(27,),(1,27)]