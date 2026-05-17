class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        
        # dp[i][j] = True if s[i:j+1] is palindrome
        dp = [[False] * n for _ in range(n)]
        
        start = 0
        max_len = 1
        
        # All single characters are palindromes
        for i in range(n):
            dp[i][i] = True
        
        # Check for 2-character palindromes
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_len = 2
        
        # Check for length >= 3
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start = i
                    max_len = length
        
        return s[start:start + max_len]