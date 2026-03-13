class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)
        #len(nums) + 1 -> (n + 1) so n tak ka sum - sum of nums



# nums.sort()

#       for i , v in enumerate(nums):
#            if (i != v): if missing in middle
#                return v - 1

#            elif (v == len(nums) - 1): # last element then next value is missing ie in n
#                return v + 1