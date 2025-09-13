def majority(nums):
    candiate, count = None, 0
    for num in nums:
        if count == 0:
            candiate = num
        count += (1 if num == candiate else -1)
    return candiate

print(majority([3,2,3]))      
print(majority([2,2,1,1,1,2,2]))