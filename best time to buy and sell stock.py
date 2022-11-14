class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        profit = 0
        
        for sell in range(len(prices)):
            if prices[sell] < prices[buy]:
                buy = sell
                
            if (prices[sell]-prices[buy]) > profit:
                profit = prices[sell]-prices[buy]
                
        return profit