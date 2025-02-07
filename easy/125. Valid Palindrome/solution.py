class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''
        for c in s:
            if c.isalpha() or c.isdigit():
                res+=c.lower()
            
        return res == res[::-1]
