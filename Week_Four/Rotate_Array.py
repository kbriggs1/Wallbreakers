class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        w = collections.deque()
        for i in nums:
            w.append(i)
        for i in range(k):
            x = w.pop()
            w.appendleft(x)
        for i in range(len(nums)):
            nums[i] = w[i]
