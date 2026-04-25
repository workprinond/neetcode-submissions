class Solution:
    def isValid(self, s: str) -> bool:
        
        stack =[]


        for c in s:
            if c == '[' :
                stack.append(']')
            elif c == '{': 
                stack.append('}')
            elif c == '(': 
                stack.append(')')
            elif c in ')]}':
                if not stack:
                    return False
                if  c == stack[-1]:
                    stack.pop()
                else:
                    return False         
           

        return len(stack) == 0
            
            

