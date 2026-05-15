from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        if not grid or not grid[0]:
            return None

        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        time= 0
        freshcount = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
                if grid[i][j] == 1:
                    freshcount += 1

        if freshcount == 0:
            return 0

        while queue:
            row,col,time = queue.popleft()

            for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr = dr + row
                nc = dc + col
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1:
                    freshcount -= 1
                    grid[nr][nc] = 2
                    queue.append((nr,nc,time + 1))

        if freshcount > 0:
            return -1

        return time

                    
