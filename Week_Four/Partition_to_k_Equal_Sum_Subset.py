class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        nums_sum = sum(nums)
        nums_size = len(nums)
        
        if nums_sum % k != 0:
            return False
        
        eachpart = nums_sum/k
        parts = [eachpart for i in range(k)]
        
        nums = sorted(nums)[::-1]
        
        def DFS(pos, parts):
            if pos == nums_size:
                return True
            
            for i, p in enumerate(parts):
                if p >= nums[pos]:
                    if parts[i] == eachpart and (i-1>=0 and parts[i-1] == eachpart):
                        break
                        
                    parts[i] -= nums[pos]                                            
                    if DFS(pos+1, parts):
                        return True
                    parts[i] += nums[pos]
            
            return False
        
        return DFS(0, parts)
