class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums) - 1
        

        while(left < right):
            mid = (left + right)//2

            if nums[mid] < nums[mid + 1]:
                left = mid + 1

            else:
                right =  mid  
                
        return left




# nums[mid] < nums[mid + 1]
# The slope is going up → a peak must exist to the right.

# nums[mid] > nums[mid + 1]
# The slope is going down → a peak exists at mid or to the left.


#  Time complexity O(log n)