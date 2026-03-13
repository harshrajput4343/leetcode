class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        for i , v in enumerate(nums):
            if (i != v):
                return v - 1

            elif (v == len(nums) - 1): # last element then next value is missing ie in n
                return v + 1