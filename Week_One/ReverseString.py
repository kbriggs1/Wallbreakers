class Solution(object):
    def reverseString(self, s):
        
        k = 0
        c = len(s)-1
        while k < c:
            tmp = s[k]
            s[k] = s[c]
            s[c] = tmp
            k += 1
            c -= 1
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
