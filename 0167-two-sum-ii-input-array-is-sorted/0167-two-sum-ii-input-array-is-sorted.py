class Solution:
    def twoSum(self, numbers: List[int], target: int ) -> List[int]:
        n = len(numbers)
        left = 0
        right = n - 1  # python uses 0 based indexes
        # use 2 pointer
        while (left < right): # ! <= we want different index
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left+1,right+1] # python uses 0 based indexes and it wantt index not number
            elif (current_sum > target):
                right -= 1
            else:
                left += 1
        return []
