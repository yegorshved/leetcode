from typing import List
from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # if there's only one word in a list, return it
        if (len(words) == 1):
            return list(words[0])

        # creating a hashmap to store frequencies of chars in first word
        counter = Counter(words[0])
        words.remove(words[0])
        # result = []
        for word in words:
            word_counter = Counter(word)
            for i in counter:
                if i in word_counter:
                    counter[i] = word_counter[i] if word_counter[i] < counter[i] else counter[i]
                else:
                    counter[i] = 0
        result = []
        for i in counter:
            if counter[i] > 0:
                while counter[i] > 0:
                    result.append(i)
                    counter[i]-=1

        return result
