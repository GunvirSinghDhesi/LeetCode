class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        toExplore=[]
        

        def bfs(m,n):
            if m>len(grid)-1 or n>len(grid[0])-1 or m<0 or n<0 or grid[m][n]!="1":
                return 0
            grid[m][n] = "-1" 
            bfs(m+1,n)
            bfs(m,n+1)
            bfs(m-1,n)
            bfs(m,n-1)
            return 1

            

        m=0
        while m < len(grid):
            n=0
            while n < len(grid[0]):
                # check if explored -1
                if grid[m][n] == "1":
                    grid[m][n] = "-1"
                    bfs(m+1,n)
                    bfs(m,n+1)
                    count+=1
                n+=1
            m+=1
        return count