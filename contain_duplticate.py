def contain_duplicate(nums):
    return len(nums) != len(set(nums))

nums = [1,2,3,1,6]
print(contain_duplicate(nums))