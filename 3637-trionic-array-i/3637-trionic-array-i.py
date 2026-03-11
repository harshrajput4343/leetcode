class Solution:
    def isTrionic(self, nums: List[int]) -> bool:

        n = len(nums)
        i = 0

        # climb first increasing slope
        while i+1 < n and nums[i] < nums[i+1]:
            i += 1

        p = i   # peak index

        # go down decreasing slope
        while i+1 < n and nums[i] > nums[i+1]:
            i += 1

        q = i   # valley index

        # climb again
        while i+1 < n and nums[i] < nums[i+1]:
            i += 1

        # validate positions and full traversal
        return p > 0 and q > p and q < n-1 and i == n-1