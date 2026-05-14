

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []  # Stores indices of temperatures waiting for warmer day
        
        for i in range(n):
            # While stack not empty AND current temp is warmer than temp at stack top
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # Pop the index of the colder day
                prev_index = stack.pop()
                # Calculate days difference
                result[prev_index] = i - prev_index
            
            # Push current index to stack (waiting for warmer day)
            stack.append(i)
        
        return result