from typing import List
import math

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        bravexuneth = (nums, queries)

        B = int(math.sqrt(n)) + 1

        mult = [dict() for _ in range(B + 1)]

        # process queries
        for l, r, k, v in queries:
            if k > B:
                idx = l
                while idx <= r:
                    nums[idx] = nums[idx] * v % MOD
                    idx += k
            else:
                rem = l % k

                if rem not in mult[k]:
                    mult[k][rem] = []

                start = (l - rem) // k
                end = (r - rem) // k

                mult[k][rem].append((start, v))
                mult[k][rem].append((end + 1, pow(v, MOD - 2, MOD)))

        # apply small k
        for k in range(1, B + 1):
            for rem, events in mult[k].items():
                events.sort()
                curr = 1
                ptr = 0

                for i in range(rem, n, k):
                    idx = (i - rem) // k

                    while ptr < len(events) and events[ptr][0] == idx:
                        curr = curr * events[ptr][1] % MOD
                        ptr += 1

                    nums[i] = nums[i] * curr % MOD

        # XOR
        res = 0
        for x in nums:
            res ^= x

        return res