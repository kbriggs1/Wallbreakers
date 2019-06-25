class Solution(object):
    def binaryGap(self, N):
        
        index = [k for k, b in enumerate(bin(N)) if b == '1']
        result = 0
        length = len(index) -1
        
        for k, val in enumerate(index):
            
            if k != length:
                diff = index[k + 1] - val 
                
                if diff > result:
                    result = diff


        return result

        """
        :type N: int
        :rtype:
