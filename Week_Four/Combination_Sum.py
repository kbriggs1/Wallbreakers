class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        def rec_sum(remain, at, prevs):
          if at >= len(candidates) or remain < candidates[at]:
            return []
          elif remain == candidates[at]:
            return [p+[remain] for p in prevs]
          else:
            reuse = rec_sum(remain - candidates[at], at, [p+[candidates[at]] for p in prevs])
            nouse = rec_sum(remain, at+1, prevs)
            return reuse + nouse
        return rec_sum(target, 0, [[]])
