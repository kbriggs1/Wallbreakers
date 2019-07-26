class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        n = len(board)
        m = len(board[0])
        
        def dfs(y, x, index):
            if index == len(word):
                return True
            if not 0 <= y < n or not 0 <= x < m or board[y][x] != word[index]:
                return False
            
            temp = board[y][x]
            board[y][x] = "#"
            
            for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
                i = y + dy
                j = x + dx
                if dfs(i, j, index + 1):
                    return True

            board[y][x] = temp
            return False
    
        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0):
                    return True
        return False
