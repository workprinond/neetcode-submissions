class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        if len(s) == 2:
            if s == s[::-1]:  # Check if palindrome
                return s
            else:
                return s[0]
        
        n = len(s)
        # Create list of sets to store palindromic substrings ending at each index
        dp = [set() for _ in range(n)]
        
        for i in range(n):
            dp[i].add(s[i])  # Single char palindrome
        
        longest = s[0]
        
        for i in range(n):
            for j in range(i + 1, n):
                substr = s[i:j+1]
                if substr == substr[::-1]:  # Palindrome check
                    dp[j].add(substr)
                    if len(substr) > len(longest):
                        longest = substr
        
        return longest