class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1  # Check last bit
            n >>= 1         # Right shift by 1
        return count