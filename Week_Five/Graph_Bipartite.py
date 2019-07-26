class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        def dfs(i, graph):
            for n in graph[i]:
                if n in color:
                    if color[n] != (color[i] + 1) % 2:
                        return False
                else:
                    color[n] = (color[i] + 1) % 2
                    if not dfs(n, graph):
                        return False
            return True
            
        if not graph:
            return False
        color = {}
        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
                if not dfs(i, graph):
                    return False
        return True
