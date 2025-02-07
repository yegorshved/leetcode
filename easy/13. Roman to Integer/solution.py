class Solution:
    def romanToInt(self, s: str) -> int:
        rom = {
            'I': 1, 'V': 5, 'X': 10, 
            'L': 50, 'C': 100, 'D': 500,
            'M': 1000
        }
        s = s[::-1]
        i = 0
        n = len(s)
        result = 0

        while i < n:
            current=rom[s[i]]
            result+=current
            if i != n - 1 and current > rom[s[i+1]]:
                result-=rom[s[i+1]]
                i+=1
            i+=1    

        return result        
            
