class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
      # step 1 : shift non zero element to the front 
      pos = 0
      for num in nums:
        if num != 0:
            nums[pos] = num
            pos += 1

      # step 2 : put 0 from pos  to last 
      for i in range(pos , len(nums)):
        nums[i] = 0
        