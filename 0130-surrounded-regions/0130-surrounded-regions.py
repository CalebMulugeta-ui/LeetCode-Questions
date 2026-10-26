class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        ROWS , COLS = len(board), len(board[0])

        def dfs(r,c):
            if r not in range(ROWS) or c not in range(COLS) or board[r][c]!='O':
                return 

            board[r][c] = 'T'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            return

        #Go thru parameters, convert O->T 
        for c in range(COLS):
            if board[0][c] == 'O':
                dfs(0,c)
        
        for r in range(1, ROWS):
            if board[r][0] == 'O':
                dfs(r,0)
        
        for r in range(1,ROWS):
            if board[r][COLS-1] == 'O':
                dfs(r,COLS-1)

        for c in range(1,COLS-1):
            if board[ROWS-1][c] == 'O':
                dfs(ROWS-1,c)


        #Convert O->X, Convert T->C
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'T':
                    board[r][c] = 'O'
        
    
        