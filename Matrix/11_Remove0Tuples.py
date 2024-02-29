def remove0tuple(list):
    new_list=[i for i in list if isinstance(i,int) or any(elem!=0 for elem in i) ]
    print(new_list)


remove0tuple(list=[1,2,0,(0),(0,0),(0,0,1),1])




