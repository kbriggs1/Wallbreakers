class Solution(object):
    def reverseWords(self, s):
        
          words = s.split(" ")
          for rvs, word in enumerate(words):
              words[rvs] = word[::-1]

          return " ".join(words)
