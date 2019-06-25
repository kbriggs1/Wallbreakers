class Solution(object):
    def detectCapitalUse(self, word):
 
    
         if word.upper() in word:
            return True
        
         if word.lower() in word:
            return True
        
         if len(word) > 1:
            first = word[0]
            rest = word[1:]
            if first.upper() in first and rest.lower() in rest:
                return True
        
         return False
