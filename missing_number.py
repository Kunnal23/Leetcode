def missingNumber(nums):
# TIME: O(n)  #SPACE: O(1)
    # n = len(nums)
    # totalSum = (n*(n+1))//2
    # actualSum = sum(nums)
    # return totalSum-actualSum

# TIME: O(n)  #SPACE: O(1)
    n = len(nums)
    ans = 0
    for i in range(n+1):
        ans ^= i                 #  ^ = XOR  #
    for num in nums:
        ans ^= num
    return ans

# TIME: O(n2) SPACE: O(1)
    # size = len(nums)
    # for i in range(size+1):
    #     if i in nums:
            # continue       
    #     else:
    #         return i

print(missingNumber([3,0,2,1,4]))