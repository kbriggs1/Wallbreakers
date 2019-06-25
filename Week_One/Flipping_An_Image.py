class Solution(object):
     
    def flipAndInvertImage(self, K):
        K = [i[::-1] for i in K ]
        for row_num , inner_list in enumerate(K):
            for indx, val in enumerate(inner_list):
                if val == 0:
                    K[row_num][indx] = 1
                if val == 1:
                    K[row_num][indx] = 0

        return K
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
