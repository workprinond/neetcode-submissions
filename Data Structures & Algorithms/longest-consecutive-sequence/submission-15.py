class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        unique_list = sorted(set(nums))
        count = 1
        maxcount = 1
        for i in range(1,len(unique_list)) :
            if unique_list[i] - unique_list[i-1] == 1:
                count+=1
                maxcount = max(count,maxcount)
            else:
                
                
                count = 1

        return maxcount



        