class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix:
            return 0
        
        def dfs(y, x, matrix, from_val):
            if from_val >= matrix[y][x]:
                return 0
            if dp[y][x] != 0:
                return dp[y][x]
                
            res = [0]
            for oy, ox in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                my = oy + y
                mx = ox + x
                if not (0 <= my < rows and 0 <= mx < cols):
                    continue
                
                res += dfs(my, mx, matrix, matrix[y][x]),
            
            dp[y][x] = max(res) + 1
            return dp[y][x]
            
        res = []
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0]*cols for y in range(rows)]
        
        for y in range(rows):
            for x in range(cols):
                res += dfs(y, x, matrix, matrix[y][x] - 1),
        
        return max(res)
