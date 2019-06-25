class Solution(object):
    def singleNumber(self, nums):
        
        first = nums[0]
        for k in nums[1:]:
            first = first ^ k

        return first
        """
        :type nums: List[int]
        :rtype: int
        """
