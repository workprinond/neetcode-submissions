class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxprofit = 0

        for num1 in range(0,len(prices)):

            for num2 in range(num1+1,len(prices)):

                if prices[num2] > prices[num1]:
                    maxprofit = max(maxprofit, prices[num2] - prices[num1])
                
        

        return maxprofit