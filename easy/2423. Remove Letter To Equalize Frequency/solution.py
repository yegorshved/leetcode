# Time O(n)
# Space O(1)

class Solution:
    def equalFrequency(self, word: str) -> bool:
        counter = Counter(word)
        max_char = max(counter, key=counter.get)
        counter[max_char]-=1
        j = next(iter(counter))
        
        for i in counter:
            if counter[i] != counter[j]:
                break
        else:
            return True
        
        counter[max_char]+=1
        min_char = min(counter, key=counter.get)
        counter[min_char]-=1
        
        j = next(iter(counter))
        if counter[j] == 0:
            for char in word:
                if counter[char] != 0:
                    j = char
                    break

        for i in counter:
            if counter[i] == 0:
                continue
            if counter[i] != counter[j]:
                break
        else:
            return True

        return False
