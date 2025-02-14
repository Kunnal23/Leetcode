def singleNumber(nums):
    xor = 0
    for num in nums:
        xor^=num
    return xor
nums = [2,1,2,1,4]
print(singleNumber(nums))