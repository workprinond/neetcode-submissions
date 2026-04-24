class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        dictionary = {}

        for x in nums:
            if x in dictionary:
                dictionary[x] += 1
            else:
                dictionary[x] = 1

        for k,v in dictionary.items():
            if v > (len(nums)/2):
                return k
        