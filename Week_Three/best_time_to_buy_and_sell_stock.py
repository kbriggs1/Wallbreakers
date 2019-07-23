class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <=1:
            return(0)
        low = prices[0]
        max_diff = 0
        for k in prices:
            if (k >= low):
                diff = k - low
                if (diff > max_diff):
                    max_diff = diff
            else:
                low = k
        return (max_diff)
		
        
