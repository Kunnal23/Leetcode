def maxProductArray(nums):
    res = max(nums)
    currMin,currMax=1,1
    for n in nums:
        temp = currMax*n
        currMax=max(currMax*n,currMin*n,n)
        currMin = min(temp,currMin*n,n)
        res = max(currMax,res)
    return res

nums = [-2,0,-4]
print(maxProductArray(nums))