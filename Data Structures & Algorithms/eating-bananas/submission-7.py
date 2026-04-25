class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)
        minrate = 100000000000000

        while left <=right :
            rate = (left + right)//2
            hourlist =  [(x + rate - 1) // rate for x in piles]
            hours = sum(hourlist)
            if hours <= h:
                right = rate - 1
                minrate = min(minrate, rate)
            else:
                left = rate + 1
              
            
            


        return minrate