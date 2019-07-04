class Solution:
     def wordPattern(self, pattern: str, str: str) -> bool:
        str=str.split(" ")
        if len(pattern)!=len(str):
            return False
        end={}
        for k in range(len(str)) :
            if str[k] not in end:
                if pattern[k] not in end.values():
                    end[str[k]]=pattern[k]
                else :
                    return False
            elif not end[str[k]] == pattern[k]:
                return False
        return True
   
            
