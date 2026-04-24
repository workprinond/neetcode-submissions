class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_numbers = set(nums)
        
        if len(nums) != len(set_numbers):
            return True
        else:
            return False