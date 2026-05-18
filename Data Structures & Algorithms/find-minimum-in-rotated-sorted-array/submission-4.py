from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If mid > right, minimum is in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            # Else, minimum is in the left half (including mid)
            else:
                right = mid
        
        return nums[left]