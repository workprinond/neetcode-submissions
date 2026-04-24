class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        front = 0
        back = len(s)-1
        newstr = ''
        while front < back: 
            temp = s[front] 
            s[front] = s[back]
            s[back] = temp
            front += 1
            back -= 1
            

        return s
        