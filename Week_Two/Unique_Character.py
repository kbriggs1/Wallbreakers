class Solution:
     def firstUniqChar(self, s: str) -> int:
        
        for index, char in enumerate(s):
            string = s[:index] + s[index + 1:]
            if char not in string:
                return index
        return -1
