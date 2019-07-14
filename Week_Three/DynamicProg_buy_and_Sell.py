class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:
            return 0
        dp=[]
        dp.append(0)
        max=dp[0]
        min=prices[0]
        i=1
        while i<len(prices):
            dp.append(prices[i]-min)
            if(prices[i]<min):
                min=prices[i]
            if(dp[i]>max):
                max=dp[i]
            i+=1
        return max
