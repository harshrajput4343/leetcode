class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        left = 0
        n = len(arr)

        while left + 1 < n  and arr[left] < arr[left + 1 ]:
            left += 1

        if left == 0 or left == n - 1:
            return False

        
        while left + 1 < n  and arr[left] > arr[left + 1 ]:
            left += 1

        return left == n - 1