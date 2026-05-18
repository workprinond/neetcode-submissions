from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        
        rows, cols = len(matrix), len(matrix[0])
        
        # Track if first row/col need to be zeroed
        first_row_zero = False
        first_col_zero = False
        
        # Check if first row has any zero
        for j in range(cols):
            if matrix[0][j] == 0:
                first_row_zero = True
                break
        
        # Check if first column has any zero
        for i in range(rows):
            if matrix[i][0] == 0:
                first_col_zero = True
                break
        
        # Use first row and column as markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # Mark row
                    matrix[0][j] = 0  # Mark column
        
        # Zero out rows based on markers (excluding first row)
        for i in range(1, rows):
            if matrix[i][0] == 0:
                for j in range(1, cols):
                    matrix[i][j] = 0
        
        # Zero out columns based on markers (excluding first column)
        for j in range(1, cols):
            if matrix[0][j] == 0:
                for i in range(1, rows):
                    matrix[i][j] = 0
        
        # Zero out first row if needed
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0
        
        # Zero out first column if needed
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0