class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        rows = len(board)
        cols = len(board[0])
        prefixMap = collections.defaultdict(list)
        for word in words:
            for k in range(len(word)):
                prefixMap[word[:k+1]].append(word)
        
        ans = []
        visited = set()
        
        def backTrack(board, k, j, curPrefix):
            if k < 0 or k > rows-1 or j < 0 or j > cols-1 or (k,j) in visited:
                return
            
            visited.add((k,j))
            curPrefix += board[k][j]
            if curPrefix in words and curPrefix not in ans:
                ans.append(curPrefix)
            
            if prefixMap[curPrefix] :
                backTrack(board, k+1,j, curPrefix)
                backTrack(board, k,j+1, curPrefix)
                backTrack(board, k-1,j, curPrefix)
                backTrack(board, k,j-1, curPrefix)
            
            visited.remove((k,j))
            
        for k in range(rows):
            for j in range(cols):
                if board[k][j] in words and not board[k][j] in ans:
                    ans.append(board[k][j])
                if prefixMap[board[k][j]]:
                    visited = set()
                    backTrack(board, k, j, "")
        return ans
