class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

    
        unique = sorted(set(nums))
        
    
        nums.clear()
        nums += unique
        
        return len(unique)