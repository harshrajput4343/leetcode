from collections import defaultdict
from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        pos = defaultdict(list)

        # collect indices
        for i, v in enumerate(nums):
            pos[v].append(i)

        ans = float('inf')

        # process each value group
        for indices in pos.values():
            if len(indices) < 3:
                continue

            # sliding window of size 3
            for i in range(len(indices) - 2):
                l = indices[i]
                r = indices[i + 2]
                dist = 2 * (r - l)
                ans = min(ans, dist)

        return ans if ans != float('inf') else -1