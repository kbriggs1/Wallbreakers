class Solution(object):
    def selfDividingNumbers(self, left, right):
        product = []
        for i in range(left, right+1):
            if "0" in str(i): continue
            
            is_divisble = True
            for k in str(i):
                if i % int(k) != 0:
                    is_divisble = False
                    
            if is_divisble: product.append(i)
                
        return product
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
