class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_palindrome = ''
        for i in range(n):
            l, r = i, i
            palindrome = s[l]

            # for odd length strings
            while l >= 0 and r <= (n - 1) and s[l] == s[r]:
                if len(max_palindrome) < len(palindrome):
                    max_palindrome = palindrome 
                l-=1
                r+=1
                if l>=0 and r<=(n - 1):
                    palindrome = s[l] + palindrome + s[r]

            l, r = i, i + 1
            palindrome = ''
            # for even length strings
            while l >= 0 and r <= (n - 1) and s[l] == s[r]:
                palindrome = s[l] + palindrome + s[r]
                if len(max_palindrome) < len(palindrome):
                    max_palindrome = palindrome 
                l-=1
                r+=1

        return max_palindrome
