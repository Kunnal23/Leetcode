def majorityElement(nums):
    res,count = 0,0
    for num in nums:
        if count == 0:
            res = num
        count += (1 if num==res else -1)
    return res                                            #MOORE's ALGORITHM

        # freq={}
        # m = len(nums)
        # for num in nums:
        #     if num not in freq:
        #         freq[num]=0
        #     freq[num]+=1
        # for i in range(len(freq)):
        #     if freq[i] > (m/2):
        #         return i
            

nums = [3,2,3]
print(majorityElement(nums))