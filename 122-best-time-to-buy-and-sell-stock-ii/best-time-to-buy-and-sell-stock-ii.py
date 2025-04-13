class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        minprice=prices[0]

        for i in range(1,len(prices)):
            if minprice > prices[i]:
                minprice = prices[i]
            if prices[i] > minprice:
                profit+=prices[i]-minprice
                minprice=prices[i]
        return profit