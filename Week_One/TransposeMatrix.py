class Solution(object):
   def transpose(self, A):
        r = len(A)
        product = [[None] * r for _ in range(len(A[0]))]
        for row_num , inner_list in enumerate(A):
            for indx, val in enumerate(inner_list):
                product[indx][row_num] = val

        return product
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
