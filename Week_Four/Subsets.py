class Solution:
    def subsets(self, nums):
        if not nums:
            return []

        results = [[]]

        path = []
        def dfs(i):
            for i in range(i, len(nums)):
                path.append(nums[i])
                results.append(path[:])
                dfs(i + 1)
                path.remove(nums[i])

        dfs(0)
        return results
