class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ilnd={}
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    s=(i,j)
                    ilnd[s]=1
        for i in ilnd.keys():
            try:
                ilnd[(i[0]-1,i[1])]
            except:
                count+=1
            try:
                ilnd[(i[0]+1,i[1])]
            except:
                count+=1
            try:
                ilnd[(i[0],i[1]-1)]
            except:
                count+=1
            try:
                ilnd[(i[0],i[1]+1)]
            except:
                count+=1
        return count
                
