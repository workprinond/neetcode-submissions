class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        temp = nums.copy()
        for num in temp:
            if val == num:
                nums.remove(val)

        return len(nums)

        