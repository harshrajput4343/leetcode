class Solution:
    def twoSum(self, numbers: List[int], target: int ) -> List[int]:
        nums = numbers
        left = 0
        right = len(nums) - 1 # python uses 0 based indexes 
        
        while (left <= right):
            sum = nums[left] + nums[right]

            if sum == target :
                return[left + 1,right + 1]
            elif sum > target:
                right -=1
            else:
                left += 1

            
        