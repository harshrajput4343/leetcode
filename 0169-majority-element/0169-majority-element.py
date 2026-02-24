class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        count = 0

        for num in nums:
            if count == 0:  #count 0 hai to element ko candidate assign karenge
                candidate = num

            if num == candidate : # element = candidate then count increases by 1
                count += 1

            else:
                count -=1  # element not equal then count decrease 

        return candidate