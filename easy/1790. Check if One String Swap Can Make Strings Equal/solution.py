class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        hashmap = {i: 0 for i in range(len(s1))}
        
        for i, n in enumerate(s2):       
            if n != s1[i]:
                hashmap[i] = -1

        letters = []
        for i in hashmap:
            if hashmap[i] == -1:
                letters.append(s1[i])           
        
        if (len(letters) != 2):
            return False

        letters[0], letters[1] = letters[1], letters[0]
        s = ''
        for i in hashmap:
            if hashmap[i] == -1:
                s += letters[0]
                letters.remove(letters[0])
            else:
                s += s1[i]
        
        if s == s2:
            return True
        else:
            return False
