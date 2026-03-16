class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # [1,2,3,4,1] and k = 3 size

        seen = set()
        for i , num in enumerate(nums):
            if num in seen:
                return True

            seen.add(num)
            if len(seen) > k:
                seen.remove(nums[i - k])

        return False