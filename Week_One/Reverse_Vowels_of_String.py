class Solution(object):
    def reverseVowels(self, s):
        vowels = "AEIOUaeiou"
        found_vowels = [i for i in s if i in vowels]
        s = list(s)
        
        for rvs, val in enumerate(s):
            if val in vowels:
                s[rvs] = found_vowels.pop()
                
        
        return ''.join(s)
