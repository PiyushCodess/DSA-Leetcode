class Solution:
    def singleNumber(self, nums):
        result = 0
        for n in nums:
            result ^= n
        return result
