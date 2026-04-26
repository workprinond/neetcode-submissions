class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        rightno = 1
        leftno = 1
        n = len(nums)
        leftarr = [1] * n
        rightarr = [1] * n
        for i in range(0,len(nums)):
            j = 0
            while(j < i):
                rightno *= nums[j]
                j+=1
                

            rightarr[i] = rightno
            rightno = 1

        for i in range(len(nums)-1,-1,-1,):
            j = len(nums)-1
            while(j > i):
                leftno *= nums[j]
                j-=1

            leftarr[i] = leftno
            leftno = 1

        output = []
        for y in range(0,len(nums)):
             output.append(leftarr[y] * rightarr[y])

        
        return output
            
        