import collections

class Solution:
    def permute(self, nums):
        # dp[0] = [1]
        # dp[1] = [[1, 2], [2, 1]]
		# edge case
        if not nums:
            return []
        dic = collections.defaultdict(list)
        dic[0] = [[nums[0]]]
        for i in range(1, len(nums)):
		   # Case one:  the new element append to the right of the list
            for l in dic[i-1]:
                dic[i].append([nums[i]] + l)
		    # Case two:  the new element append to the left of the list
            for l in dic[i-1]:
                dic[i].append(l + [nums[i]])
		    # Case three:  the new element somewhere between the list
            for lst in dic[i-1]:
                for x in range(1, len(lst)):
                    dic[i].append(lst[:x] + [nums[i]] + lst[x:])
        return dic[len(nums)-1]
