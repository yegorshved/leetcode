class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        counter = 0
        for i in range(n):
            l, r = i, i

            # for odd length strings
            while l >= 0 and r <= (n - 1) and s[l] == s[r]:
                counter+=1
                l-=1
                r+=1
                
            l, r = i, i+1
            
            # for even length strings
            while l >= 0 and r <= (n - 1) and s[l] == s[r]:
                counter+=1
                
                l-=1
                r+=1

        return counter

