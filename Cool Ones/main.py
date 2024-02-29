import itertools
lst=[[1,2,3],[4,5,6]]
crossProducts=list(itertools.product(*lst))
print(crossProducts)


