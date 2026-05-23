class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n # [-1,-1,-1]
        stack = []

        for i in range (2*n-1, -1,-1): # for circular array
            num = nums[i % n]

            while stack and stack[-1] <= num:
                stack.pop()

            if i < n:  # for answer in second half
                if stack:
                    ans[i] = stack[-1] # possible next greater element becoz smaller poped
                else:
                    ans[i] = -1
            stack.append(num)

        return ans