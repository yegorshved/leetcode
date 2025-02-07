class Solution:
    def isAnagram(self, str1: str, str2: str) -> bool:
        if (len(str1) != len(str2)):
            return False
        counter = [0] * 26 # English alphabet!
        for i in range(len(str1)):
            counter[ord(str1[i]) - ord('a')] += 1
            counter[ord(str2[i]) - ord('a')] -= 1
        for i in counter:
            if i != 0:
                return False
        return True
