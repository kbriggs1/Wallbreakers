class Solution(object):
    def sortArrayByParity(self, A):
        
        result = []
        for i in A:
            if i % 2 == 0:
                result.insert(0,i)
            else:
                result.append(i)
        return result
        """
        :type A: List[int]
        :rtype: List[int]
        """
