def custom_counter(words: List[str]) -> dict:
    hmap = {}
    for i in words:
        if not i in hmap:
            hmap[i] = 1
        else:
            hmap[i]+=1
    return hmap
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        # frequencies of words in each list
        freq1 = custom_counter(words1)
        freq2 = custom_counter(words2)
        print(freq1)
        print(freq2)

        # counter for words that match condition
        counter = 0
        for i in freq1:
            if i in freq2 and freq1[i] == 1 and freq2[i] == 1:
                counter+=1
        return counter
