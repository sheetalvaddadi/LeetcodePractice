import collections
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands =0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] =="1":
                    self.bfs(grid, i,j)
                    num_islands+=1
        return num_islands
    
    def bfs(self, grid, i,j):
        q = collections.deque()
        q.appendleft((i,j))
        
        while(q):
            row,col = q.pop()
            
            if row+1 < len(grid) and grid[row+1][col] =="1":
                grid[row+1][col] = "0"
                q.appendleft((row+1,col))
            if row-1 >=0 and grid[row-1][col] =="1":
                grid[row-1][col] = "0"
                q.appendleft((row-1,col))
            if col+1 < len(grid[0]) and grid[row][col+1] =="1":
                grid[row][col+1] = "0"
                q.appendleft((row,col+1))
            if col-1 >=0 and grid[row][col-1] =="1":
                grid[row][col-1] = "0"
                q.appendleft((row,col-1))

        