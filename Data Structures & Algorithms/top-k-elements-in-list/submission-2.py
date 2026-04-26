class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dic = {}
        
        for i in nums:
            dic[i] = dic.get(i, 0) + 1

        newlst = []  
        for i,(key, value) in enumerate(sorted(dic.items(), key=lambda x: x[1], reverse = True)):
            if (i<k):
                newlst.append(key)

        return newlst if newlst else [] 
