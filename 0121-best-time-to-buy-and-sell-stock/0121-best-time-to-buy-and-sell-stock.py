class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # [7,1,5,3,6,4]

        l , r = 0, 1
        maxP = 0


        while r != len(prices):
            if prices[l] < prices[r]:
                prof = prices[r] - prices[l]
                maxP = max(maxP , prof)
            else:
                l = r

            r += 1

        return maxP