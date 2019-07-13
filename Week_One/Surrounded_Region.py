class Solution(object):
    def solve(self, board):
        
        if len(board) <= 1:
            return
        
        a, b = len(board), len(board[0])
        qu = collections.deque()

        for i in xrange(a):
            if board[i][0] == "O":
                qu.append(i * b)
            
            if board[i][-1] == "O":
                qu.append((i + 1) * b - 1)
        
        for i in xrange(b):
            if board[0][i] == "O":
                qu.append(i)
            
            if board[-1][i] == "O":
                qu.append((a - 1) * b + i)
    
        
        while len(qu) != 0:
            loc = qu.popleft()
            row, col = loc // b, loc % b
            if board[row][col] == "K":
                continue

            board[row][col] = "K"
            dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
            for i in xrange(4):
                nextRow, nextCol = row + dy[i], col + dx[i]
                if self.istrue(nextRow, nextCol, board):
                    qu.append(nextRow * b + nextCol)
        
        for i in xrange(a):
            for j in xrange(b):
                if board[i][j] != "K":
                    board[i][j] = "X"
                else:
                    board[i][j] = "O"
    
    def istrue(self, a, b, board):
        if a < 0 or a >= len(board) or b < 0 or b >= len(board[0]) or board[a][b] == "X" or board[a][b] == "K":
            return False
        return True
