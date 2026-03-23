class Solution:
    def maxProductPath(self, grid):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # dp_max[i][j] = max product till (i,j)
        # dp_min[i][j] = min product till (i,j)
        dp_max = [[0]*n for _ in range(m)]
        dp_min = [[0]*n for _ in range(m)]

        dp_max[0][0] = dp_min[0][0] = grid[0][0]

        # first row
        for j in range(1, n):
            val = grid[0][j]
            dp_max[0][j] = dp_min[0][j] = dp_max[0][j-1] * val

        # first col
        for i in range(1, m):
            val = grid[i][0]
            dp_max[i][0] = dp_min[i][0] = dp_max[i-1][0] * val

        # fill rest
        for i in range(1, m):
            for j in range(1, n):
                val = grid[i][j]

                # possible values from top and left
                candidates = [
                    dp_max[i-1][j] * val,
                    dp_min[i-1][j] * val,
                    dp_max[i][j-1] * val,
                    dp_min[i][j-1] * val
                ]

                dp_max[i][j] = max(candidates)
                dp_min[i][j] = min(candidates)

        res = dp_max[m-1][n-1]

        return res % MOD if res >= 0 else -1