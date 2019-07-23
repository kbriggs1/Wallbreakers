class Solution:
      def rob(self, houses):
        k = len(houses)
        if k == 0:
            return 0
        if k <= 2:
            return max(houses)
        a = b = c = d = 0
        house = 0
        for i, x in enumerate(houses):
            if i < k-1:
                a, b = b, max(x+a, b)
            if i > 0:
                c, d = d, max(x+c, d)
            house = max(house, b, d)
        return house
