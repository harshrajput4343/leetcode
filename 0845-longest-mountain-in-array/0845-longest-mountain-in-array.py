class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        result = 0

        for i in range(1,len(arr)-1): # traversing from 2nd element to 2nd last element, ie. mountain peak can not be 1st and last  

            if arr[i - 1] < arr[i] > arr[i + 1]:  # peak element

                l=r=i
                while l > 0 and arr[l] > arr[l-1]: # going left from peak
                    l-= 1
                
                while r < len(arr)-1 and arr[r] > arr[r+1]: # going right from peak
                    r += 1

                result = max(result,r-l+1)
                
        return result
