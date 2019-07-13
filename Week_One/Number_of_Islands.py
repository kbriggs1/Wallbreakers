class Solution(object):
    def numIslands(self, grid):
        if len(grid) == 0:
            return 0
        K, A = [-1, 1, 0, 0], [0, 0, 1, -1]
        b, c = len(grid), len(grid[0])
        def dfs(k, a):
            grid[k][a] = '2' # visited
            for i in range(4):
                ck, ca = k + K[i], a + A[i]
                if ck >= 0 and ck < len(grid) and ca >= 0 and ca < len(grid[0]) and grid[ck][ca] == '1':
                    dfs(ck, ca)
        result = 0
        for i in range(b):
            for j in range(c):
                if grid[i][j] == '1':
                    dfs(i, j)
                    result += 1
        return result
