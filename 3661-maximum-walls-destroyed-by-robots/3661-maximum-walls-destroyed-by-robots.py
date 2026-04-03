from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        bots = sorted(zip(robots, distance))
        n = len(bots)
        ws = sorted(walls)

        def count(lo, hi):
            if lo > hi:
                return 0
            return bisect_right(ws, hi) - bisect_left(ws, lo)

        # Walls exactly at robot positions (always destroyable)
        at_pos_total = sum(count(p, p) for p, _ in bots)

        # Single robot case
        if n == 1:
            pos, dist = bots[0]
            at = count(pos, pos)
            extra_l = count(pos - dist, pos - 1)
            extra_r = count(pos + 1, pos + dist)
            return at + max(extra_l, extra_r)

        R, L, U = [], [], []

        for i in range(n - 1):
            pl, dl = bots[i]
            pr, dr = bots[i + 1]

            gap_lo, gap_hi = pl + 1, pr - 1

            r_reach = min(pl + dl, gap_hi)
            l_reach = max(pr - dr, gap_lo)

            # Right robot i → gap
            R.append(count(gap_lo, r_reach))

            # Left robot i+1 → gap
            L.append(count(l_reach, gap_hi))

            # ---- FIXED UNION LOGIC ----
            if r_reach < l_reach - 1:
                # disjoint
                u = count(gap_lo, r_reach) + count(l_reach, gap_hi)
            else:
                # overlapping or touching
                u = count(min(gap_lo, l_reach), max(r_reach, gap_hi))

            U.append(u)

        # Outer regions
        p0, d0 = bots[0]
        outer_left = count(p0 - d0, p0 - 1)

        pn, dn = bots[-1]
        outer_right = count(pn + 1, pn + dn)

        # DP initialization
        dp = [
            max(outer_left + L[0], U[0]),  # next robot fires left
            max(outer_left, R[0])          # next robot fires right
        ]

        # DP over gaps
        for i in range(1, n - 1):
            is_last = (i == n - 2)
            or_i = outer_right if is_last else 0

            dp = [
                max(dp[0] + L[i], dp[1] + U[i]),
                max(dp[0] + or_i, dp[1] + R[i] + or_i)
            ]

        return at_pos_total + max(dp)