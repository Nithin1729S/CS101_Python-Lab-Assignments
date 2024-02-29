L1=[(1,1,1,1,1,5,6,7),(1,1,1,11,1,1,11),(1,2,3,4,5,6,7,8),(1,)]
L1=[tuple(set(i)) for i in L1]
L1.sort(key=len)
print(L1)
