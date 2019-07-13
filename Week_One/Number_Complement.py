class Solution(object):
    def findComplement(self, num):
        output = ""
        num = bin(num)[2:]
        for k in num:
            output += "0" if k == "1" else "1"
        
        return int(output, 2) 
        """
        :type num: int
        :rtype: int
        """
