def maxSubArray(nums):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] <= nums[right]:
            right = mid
        else:
            left = mid + 1
    return nums[left]
    # sl = sorted(nums)
    # return sl[0]
nums = [11,13,15,17]
print(maxSubArray(nums))