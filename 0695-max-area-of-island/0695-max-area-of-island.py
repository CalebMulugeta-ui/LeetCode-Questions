class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """ 
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(grid, r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0):
                return 0

            currArea = 1
            grid[r][c] = 0
            currArea += dfs(grid, r+1, c)
            currArea += dfs(grid, r-1, c)
            currArea += dfs(grid, r, c+1)
            currArea += dfs(grid, r, c-1)
            return currArea
        
        maxArea = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = dfs(grid, r, c)
                    if maxArea < area:
                        maxArea = area

        return maxArea




        