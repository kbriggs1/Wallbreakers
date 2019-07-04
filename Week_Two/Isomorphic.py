class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapping = {}
        set_ = set()
        for k in range(len(s)):
            
            if s[k] not in mapping and t[k] in set_:
                return False
            
            elif s[k] not in mapping:
                mapping[s[k]] = t[k]
                set_.add(t[k])
                
            elif mapping[s[k]] != t[k]:
                return False
