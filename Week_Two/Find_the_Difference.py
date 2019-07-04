class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        asc = 0
        for char in t:
            asc += ord(char) 
        
        for char in s:
            asc -= ord(char) 
            
        return chr(asc)
