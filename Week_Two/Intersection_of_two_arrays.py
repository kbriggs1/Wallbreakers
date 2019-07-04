class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        short = nums1
        long = nums2
        if len(short) > len(long):
            long = nums1
            short = nums2
            
        output = []
        for i in short:
            if i in long and i not in output:
                output.append(i)
            
        return output
