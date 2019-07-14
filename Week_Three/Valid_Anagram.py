#Second best solution 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        if(len(s)==0 and len(t)==0):
            return True
        set_s = set(s)
        set_t = set(t)
        for i in set_s:
            if(t.count(i) != s.count(i)):
                return False
        return True
