def hammingWeight(n):
    # BRUTE FORCE APPROACH (SPACE:O(logn))
    # binary = bin(n)[2:]
    # lst = list(binary)
    # count=0
    # for item in lst:
    #     if item == '1':
    #         count+=1
    # return count
# SPACE:O(1)
    # res =0
    # while n:
    #     res+= n%2
    #     n = n >> 1
    # return res

    res=0
    while n:
        n = n&(n-1)
        res+=1
    return res

print(hammingWeight(5))