class Solution(object):
    def twoSum(self, nums, target):
        for k, val in enumerate(nums):
            for k2, val2 in enumerate(nums[k+1:]):
                if val + val2 == target:
                    return [k, k2 + k +1]
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
