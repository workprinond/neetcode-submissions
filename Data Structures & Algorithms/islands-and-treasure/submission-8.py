from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        if not grid or not grid[0]:
            return None

        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i,j,0))

        
        while queue:
            row,col,distance = queue.popleft()

            for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr = dr + row
                nc = dc + col
                if (0<=nr<rows and 0<=nc<cols and grid[nr][nc]==2147483647):
                    grid[nr][nc]= distance + 1
                    queue.append((nr,nc,distance+1))
            


        