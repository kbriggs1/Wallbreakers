class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums) - 1)
    def binary_search(self, nums, target, low, high):
        mid = (low + high) // 2
        if high < low:
            return -1
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.binary_search(nums, target, low, mid -1)
        else:
            return self.binary_search(nums, target, mid + 1, high)
