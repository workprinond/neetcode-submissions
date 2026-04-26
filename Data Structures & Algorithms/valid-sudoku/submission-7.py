class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

         for row in board:
            seen = set()
            for cell in row:
                if cell != '.':
                    if cell in seen:
                        return False
                    seen.add(cell)
      
         for col in zip(*board):
            seen = set()
            for cell in col:
                if cell != '.':
                    if cell in seen:
                        return False
                    seen.add(cell)
     
         for i in range(0,9,3):
                for j in range(0,9,3):
                    seen = set()
                    for x in range(i, i + 3):
                        for y in range(j, j + 3):
                            cell = board[x][y]
                            if cell != '.':
                                if cell in seen:
                                    return False
                                seen.add(cell)



         return True


        

    