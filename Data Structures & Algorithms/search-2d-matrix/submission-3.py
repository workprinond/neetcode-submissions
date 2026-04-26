class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
      flat_list = [item for sublist in matrix for item in sublist]

      left = 0
      right = len(flat_list) - 1

      while(left<=right):
        mid = (left + right)//2
        if target == flat_list[mid]:
            return True
        if target <= flat_list[mid]:
            right = right - 1
        else:
            left = left + 1

        
      return False 