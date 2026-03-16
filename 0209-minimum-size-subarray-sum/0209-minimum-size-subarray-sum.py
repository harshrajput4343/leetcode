class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # [2,3,1,2,4,3]  ; target = 7

        l = 0
        total_sum = 0
        res = float('inf')

        for r in range(len(nums)):
            total_sum += nums[r]
            while total_sum >= target:
                res = min(res,r - l +1)

                total_sum -=  nums[l]
                l += 1

        if res == float('inf'):
            return 0
        else:
            return res

        