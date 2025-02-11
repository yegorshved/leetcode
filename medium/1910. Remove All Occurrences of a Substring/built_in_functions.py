class Solution:

    def removeOccurrences(self, s: str, part: str) -> str:
        inx = s.find(part)
        while inx != -1:
            print(s)
            s = s.replace(part, '', 1)
            inx = s.find(part)
        return s


