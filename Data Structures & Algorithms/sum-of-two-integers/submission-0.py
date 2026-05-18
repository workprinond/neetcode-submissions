class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32-bit mask to handle negative numbers
        MASK = 0xFFFFFFFF
        
        while b != 0:
            # Calculate carry (bits where both a and b are 1)
            carry = (a & b) & MASK
            
            # Sum without carry (XOR)
            a = (a ^ b) & MASK
            
            # Shift carry to left
            b = (carry << 1) & MASK
        
        # Handle negative numbers (if a is negative in 32-bit representation)
        return a if a <= 0x7FFFFFFF else ~(a ^ MASK)
        