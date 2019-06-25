class Solution(object):
    def hammingDistance(self, x, y):
        dist = 0
        val = x ^ y

        while val > 0:
            if val & 1:
                dist += 1

            val //=2

        return dist
        """
        :type x: int
        :type y: int
        :rtype: int
        """
