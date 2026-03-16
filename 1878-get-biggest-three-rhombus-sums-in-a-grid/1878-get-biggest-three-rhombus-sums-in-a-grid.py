from typing import List

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])

        dp  = [[0] * n for _ in range(m)]
        dp2 = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                dp[r][c]  = grid[r][c] + (dp[r-1][c-1]  if r>0 and c>0   else 0)
                dp2[r][c] = grid[r][c] + (dp2[r-1][c+1] if r>0 and c<n-1 else 0)

        def seg_dr(r1, c1, r2, c2):
            """↘ segment: (r1,c1) to (r2,c2), r-c = const"""
            res = dp[r2][c2]
            if r1 > 0 and c1 > 0:
                res -= dp[r1-1][c1-1]
            return res

        def seg_dl(r1, c1, r2, c2):
            """↙ segment: (r1,c1) to (r2,c2), r+c = const"""
            res = dp2[r2][c2]
            if r1 > 0 and c1 < n-1:
                res -= dp2[r1-1][c1+1]
            return res

        def rhombus_sum(r, c, s):
            if s == 0:
                return grid[r][c]

            top, bot   = r - s, r + s
            left, right = c - s, c + s

            # Each edge INCLUDES both its endpoint corners
            # So all 4 corners are counted exactly twice → subtract all 4 once
            tl = seg_dl(top, c,    r,   left)   # (top,c) ↙→ (r,left)
            tr = seg_dr(top, c,    r,   right)  # (top,c) ↘→ (r,right)
            lb = seg_dr(r,   left, bot, c)      # (r,left) ↘→ (bot,c)
            rb = seg_dl(r,   right,bot, c)      # (r,right) ↙→ (bot,c)

            # ✅ Subtract all 4 corners (each counted twice across the 4 edges)
            return (tl + tr + lb + rb
                    - grid[top][c]   # shared by tl + tr
                    - grid[bot][c]   # shared by lb + rb
                    - grid[r][left]  # shared by tl + lb
                    - grid[r][right])# shared by tr + rb

        top3 = set()

        for r in range(m):
            for c in range(n):
                max_s = min(r, c, m-1-r, n-1-c)
                for s in range(max_s + 1):
                    top3.add(rhombus_sum(r, c, s))
                    if len(top3) > 3:
                        top3.remove(min(top3))

        return sorted(top3, reverse=True)