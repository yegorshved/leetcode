class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if (len(s) > len(t)):
            return False
        counter_t = 0
        counter_s = 0
        while counter_t < len(t) and counter_s < len(s):
            if s[counter_s] == t[counter_t]:
                counter_s+=1
            counter_t+=1

        
        return counter_s == len(s)
