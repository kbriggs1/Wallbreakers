class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = {i:[] for i in range(numCourses)}
        
        indeg = [0 for i in range(numCourses)]
        
        for x,y in prerequisites:
            edges[y].append(x)
            indeg[x]+=1
            
        que = collections.deque()
        
        
        for i in range(len(indeg)):
            if indeg[i] == 0:
                que.append(i)
        res = 0
        while que:
            x = que.popleft()
            res+=1
            for n in edges[x]:
                indeg[n] -= 1
                if indeg[n] == 0:
                    que.append(n)
                
            
            
            
            
        return res==numCourses
