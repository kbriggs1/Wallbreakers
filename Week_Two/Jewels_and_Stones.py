class Solution:
    #define
    def numJewelsInStones(self, J, S):
      count = 0
      for char in S:
        if char in J:
          count += 1

      return count



J1 = "aA" 
S1 = "aAAbbbb"
J = "z"
S = "ZZ"

