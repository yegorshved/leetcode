class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ' and counter != 0:
                break
            elif s[i] == ' ' and counter == 0:
                continue
            else:
                counter+=1

        return counter
