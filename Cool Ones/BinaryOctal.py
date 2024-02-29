
def binary(n):
    bins=[]
    while n!=0:
        bins.append(n%2)
        n=n//2
    bins=reversed([str(i) for i in bins])
    binary_num="".join(bins)
    return binary_num
print(binary(24))

def decimal(num):
    nums=[]
    num=str(num)
    for char in num:
        nums.append(int(char))
    sum_=0
    for idx,digit in enumerate(num,start=-len(num)+1):
        sum_+=int(digit)*(2**abs(idx))
    print(sum_)
decimal(11000)





