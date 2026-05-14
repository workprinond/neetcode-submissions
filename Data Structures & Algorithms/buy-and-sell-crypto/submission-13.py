class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0  # Buy day
        maxprofit = 0
        
        for right in range(1, len(prices)):  # right = sell day
            # If price drops, move buy day to current day
            if prices[right] < prices[left]:
                left = right
            else:
                # Calculate profit if selling today
                profit = prices[right] - prices[left]
                maxprofit = max(maxprofit, profit)
        
        return maxprofit