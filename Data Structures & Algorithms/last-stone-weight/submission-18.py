class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        newstones = stones.copy()
        while len(newstones) > 1 :
            newstones.sort()
            if newstones[-1] == newstones[-2]:
                newstones.pop()
                newstones.pop()
            else: 
              
                newstones[-1] = newstones[-1] - newstones[-2]
                newstones.pop(-2)


        return newstones[0] if newstones else 0