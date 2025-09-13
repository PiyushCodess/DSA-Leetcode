def disappearElements(nums):
    for num in nums:
        index = abs(num) - 1
        if nums[index] > 0:
            nums[index] *= -1

    return[i+1 for i, num in enumerate(nums) if num > 0]

print(disappearElements([4,3,2,7,8,2,3,1]))