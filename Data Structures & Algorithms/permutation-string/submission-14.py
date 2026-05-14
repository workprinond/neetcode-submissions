class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
    
        

        left=0
        window={}
        windowsub={}
        for i in range(len(s1)):
            window[s1[i]] = window.get(s1[i],0) + 1

        for right in range(len(s1)-1,len(s2)):

            sub = s2[left:right+1]

           
            for i in range(len(sub)):
                windowsub[sub[i]] = windowsub.get(sub[i],0) + 1


            if windowsub == window:
                return True
            else:
                left+=1
                windowsub.clear()

        return False



        