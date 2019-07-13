class Solution(object):
    def longestCommonPrefix(self, strs):
    
            if not strs: return ''
            st1 = min(strs)
            st2 = max(strs)

            for i, k in enumerate(st1):
                 if k != st2[i]:
                     return st1[:i]
            return st1



story = ["flower","flow","flight"]
story1 = ["rog","racecar","caar"]
story2 = ["bbc","cc","ba"]
print((story2))
