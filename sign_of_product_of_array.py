def arraySign(nums):
    sign = 1
    for num in nums:
        if num == 0:
            return 0
        elif num < 0:
            sign *= -1
    return sign

print(arraySign([1,5,0,2,-3]))  