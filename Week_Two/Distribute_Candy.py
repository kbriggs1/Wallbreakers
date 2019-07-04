class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        candy=len(set(candies))
    
        if candy> len(candies)//2:
           return len(candies)//2
        else:
           return candy
