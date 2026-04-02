from typing import List

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        INF = float('-inf')
        
        # dp[j][k] = current row
        dp = [[INF]*3 for _ in range(n)]
        
        # init (0,0)
        for k in range(3):
            if coins[0][0] >= 0:
                dp[0][k] = coins[0][0]
            else:
                dp[0][k] = 0 if k > 0 else coins[0][0]
        
        # first row
        for j in range(1, n):
            for k in range(3):
                if coins[0][j] >= 0:
                    dp[j][k] = dp[j-1][k] + coins[0][j]
                else:
                    take = dp[j-1][k] + coins[0][j]
                    neutralize = dp[j-1][k-1] if k > 0 else INF
                    dp[j][k] = max(take, neutralize)
        
        # rest rows
        for i in range(1, m):
            new_dp = [[INF]*3 for _ in range(n)]
            
            # first column
            for k in range(3):
                if coins[i][0] >= 0:
                    new_dp[0][k] = dp[0][k] + coins[i][0]
                else:
                    take = dp[0][k] + coins[i][0]
                    neutralize = dp[0][k-1] if k > 0 else INF
                    new_dp[0][k] = max(take, neutralize)
            
            # rest
            for j in range(1, n):
                for k in range(3):
                    best_prev_k = max(dp[j][k], new_dp[j-1][k])
                    
                    if coins[i][j] >= 0:
                        new_dp[j][k] = best_prev_k + coins[i][j]
                    else:
                        take = best_prev_k + coins[i][j]
                        neutralize = INF
                        if k > 0:
                            best_prev_km1 = max(dp[j][k-1], new_dp[j-1][k-1])
                            neutralize = best_prev_km1
                        new_dp[j][k] = max(take, neutralize)
            
            dp = new_dp
        
        return max(dp[n-1])