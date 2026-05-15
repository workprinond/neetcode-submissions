from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:


        rows = len(grid)
        cols = len(grid[0])

        max_area = 0
        queue = deque()

        def bfs(r,c):
            area = 0
            queue.append((r,c))
            grid[r][c] = 0
            while queue:
                row, col = queue.popleft()
                area +=1
                for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nr = row + dr
                    nc = col + dc
                    if 0<=nr<rows and 0 <=nc<cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        queue.append((nr,nc))
            return area




        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_area = max(max_area,bfs(i,j))
        


        return max_area