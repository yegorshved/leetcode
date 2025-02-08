class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        strs.sort()
        s1 = strs[0]
        s2 = strs[-1]
        inx = 0
        while inx < len(s1) and inx < len(s2):
            if s1[inx] == s2[inx]:
                inx+=1
            else:
                break
        return strs[0][:inx]
