class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 1000000007
        arr = nums  # local reference (faster)

        for l, r, k, v in queries:
            for i in range(l, r + 1, k):
                arr[i] = (arr[i] * v) % MOD

        res = 0
        for x in arr:
            res ^= x

        return res
        