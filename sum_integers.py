def getSum(a,b):
    mask = 0xffffffff
    while(mask&b)>0:
        a,b=a^b,(a&b)<<1
    return (mask&a) if b>0 else a
        # return sum([a,b])
print(getSum(9,-8))