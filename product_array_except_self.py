
def productExceptSelf(nums):
    # TIME COMPLEXITY : O(n^2)
    # arr=[]
    # temp = nums
    # for i in range(len(nums)):
    #     product = 1
    #     for j in range(len(nums)):
    #         if i != j:
    #             product = product * temp[j]
    #     arr.append(product)
    # print(arr) 

    # TIME COMPLEXITY : O(n)         
    arr=[1]*len(nums)
    prefix = 1
    for i in range(len(nums)):
        arr[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums)-1,-1,-1):
        arr[i] *= postfix
        postfix *= nums[i]
    return arr
        
nums=[1,2,3,4]
print(productExceptSelf(nums))