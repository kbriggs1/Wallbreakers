class Solution:
     def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        k1,k2,k3 = 0,0,0
        for i in bills:
            if i == 5:
                k1 += 1
            elif i == 10 and k1: 
                k1 -= 1
                k2 += 1
            elif i == 20 and k1 and k2:
                k3 += 1
                k2 -= 1
                k1 -= 1
            elif i == 20 and k1 > 2:
                k3 += 1
                k1 -= 3      
            else:
                return False
        return True
        
