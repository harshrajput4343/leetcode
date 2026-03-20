class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]*(n+1)

        offset = 1

        for i in range(1,n + 1):
            if offset*2 == i: #  logic 1, 2, 4, 8   (i.e 2 power 0,1,2,3)
                offset = i

            dp[i] = 1 + dp[i - offset]

        return dp