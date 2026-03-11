class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)        # store nums1 elements for O(1) lookup
        result = set()           # store unique intersection elements

        for num in nums2:
            if num in set1:      # check if element exists in nums1
                result.add(num)  # add to result (set keeps unique)

        return list(result)      # convert set to list