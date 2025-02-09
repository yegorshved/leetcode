class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        n = len(words)
        result = []
        for word in words:
            temp = set(word.lower())
            if temp <= row3 or temp <= row2 or temp <= row1:
                result.append(word)

        return result
