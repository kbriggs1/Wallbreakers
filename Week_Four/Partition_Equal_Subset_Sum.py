class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mysum = sum(nums)
        if mysum%2 or len(nums)<2: return False
        nums.sort()
        return self.helper(nums,mysum/2)
    
    def helper(self,nums,target):
        if not target: return True
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]: continue
            if target>=nums[i] and self.helper(nums[i+1:],target-nums[i]):  return True
        return False
        
