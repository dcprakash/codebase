'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solution/

The points of interest are the peaks and valleys in the given graph. 
We need to find the largest peak following the smallest valley. 
We can maintain two variables - minprice and maxprofit corresponding to the smallest valley and maximum profit (maximum difference between selling price and minprice) obtained so far respectively.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                    max_profit = max(prices[j] - prices[i], max_profit)
        return max_profit

    def maxProfitEff(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
                
        return max_profit