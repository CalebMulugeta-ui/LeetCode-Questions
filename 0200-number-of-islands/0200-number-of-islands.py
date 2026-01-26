class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        def dfs(grid, r, c):
            if(r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0"):
                return
            
            grid[r][c] = "0"
            dfs(grid,r+1 , c)
            dfs(grid,r-1, c)
            dfs(grid,r, c+1)
            dfs(grid, r, c-1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(grid, r, c)
                    islands+=1
            
           
        return islands




                
        