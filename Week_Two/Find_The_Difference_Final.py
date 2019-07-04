#Find the difference.py
class Solution:
    def findTheDifference(self, s, t):
        
        for k in t:
            if k not in s or s.count(i) != t.count(k):
                return k 
