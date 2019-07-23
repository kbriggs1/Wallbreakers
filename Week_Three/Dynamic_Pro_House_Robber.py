class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        
        if N == 0:
            return 0
        
        if N <= 3:
            return max(nums)
        
        prev = 0
        curr = 0
        
        prevNo = 0
        currNo = 0
        
        for i, num in enumerate(nums):
            # excluding last index
            if i < N-1:
                tmp = curr            
                curr = max(prev+num, curr)
                prev = tmp
            
            # excluding first index
            if i > 0:
                tmpNo = currNo
                currNo = max(prevNo+num, currNo)
                prevNo = tmpNo
                
        return max(curr, currNo)
