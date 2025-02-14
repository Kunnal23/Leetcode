def countBits(n):
    arr=[]
    for i in range(n+1):
        res=0
        while i:
            i = i&(i-1)
            res+=1
        arr.append(res)
    return arr

print(countBits(5))