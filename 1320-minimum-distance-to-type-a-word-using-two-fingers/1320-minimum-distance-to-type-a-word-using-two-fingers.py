class Solution:
    def minimumDistance(self, word: str) -> int:
        def dist(a, b):
            if a == -1 or b == -1:
                return 0
            x1, y1 = divmod(a, 6)
            x2, y2 = divmod(b, 6)
            return abs(x1 - x2) + abs(y1 - y2)

        n = len(word)
        nums = [ord(c) - ord('A') for c in word]

        # dp[j] = max saved distance when second finger at j
        dp = [0] * 26

        total = 0

        for i in range(1, n):
            cur = nums[i]
            prev = nums[i - 1]

            d = dist(prev, cur)
            total += d

            new_dp = dp[:]

            for j in range(26):
                # Move second finger from j -> cur
                gain = dp[j] + d - dist(j, cur)
                new_dp[prev] = max(new_dp[prev], gain)

            dp = new_dp

        return total - max(dp)