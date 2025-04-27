class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)  # Get the number of days
        
        # Initialize a 2D dp array, dp[i][0] means holding a stock on day i, dp[i][1] means not holding any stock
        dp = [[0]*2 for _ in range(length)]
        
        dp[0][0] = -prices[0]  # On day 0, if holding a stock, the profit is -prices[0] (buy the stock)
        dp[0][1] = 0           # On day 0, if not holding any stock, the profit is 0
        
        for i in range(1, length):
            # dp[i][0]: The maximum profit at day i when holding a stock
            # Two options:
            #   1. Continue holding from yesterday: dp[i-1][0]
            #   2. Buy today after selling yesterday: dp[i-1][1] - prices[i]
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            
            # dp[i][1]: The maximum profit at day i when not holding any stock
            # Two options:
            #   1. Continue not holding from yesterday: dp[i-1][1]
            #   2. Sell today after holding yesterday: dp[i-1][0] + prices[i]
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        
        # The final answer is the maximum profit when not holding any stock on the last day
        return dp[-1][1]