class Solution(object):
    def findCircleNum(self, K): 
        circles = 0
        visited = set()
        for person in range(len(K)):
            if person not in visited:
                circles += 1
                self.dfs(person, K, visited)
                
        return circles
            
            
    def dfs(self, node, K, visited):
        for person, is_friend in enumerate(K[node]):
            if is_friend and person not in visited:
                visited.add(person)
                self.dfs(person, K, visited)
        """
        :type M: List[List[int]]
        :rtype: int
        """
