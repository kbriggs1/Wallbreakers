class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        map_s = {}
        map_t = {}

        str = str.split(" ")
        if len(str) != len(pattern):
            return False
        
        for i, char_s in enumerate(pattern):
            char_t = str[i]

            if char_s not in map_s:
                map_s[char_s] = char_t

            if char_t not in map_t:
                map_t[char_t] = char_s

            if map_s[char_s] != char_t or map_t[char_t] != char_s:
                return False
        return True



pattern = "abba"
strr = "dog cat cat dog"
pattern = "abba"
strr = "dog cat cat fish"
