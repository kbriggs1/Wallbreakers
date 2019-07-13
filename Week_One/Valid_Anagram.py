class Solution(object):
    def isAnagram(self, s, t):
          if len(t) != len(s): return False
          nars1 = {}
          nars2 = {}

          for nar1, nar2 in zip(s, t):
              if nar1 not in nars1:
                nars1[nar1] = 1
              else:
                nars1[nar1] += 1

              if nar2 not in nars2:
                nars2[nar2] = 1
              else:
                nars2[nar2] += 1

          for k in nars1:
              if nars1.get(k) != nars2.get(k):
                return False

          return True
