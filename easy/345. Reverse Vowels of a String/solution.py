class Solution:
    def reverseVowels(self, s: str) -> str:
        map = {i: 0 for i in 'aeiouAEIOU'}
       # print(map)
       # s = 'IceCreAm'
        reversed_s = []

        for i in s[::-1]:
          if i in map:
            reversed_s.append(i)
        result = ''

        #print(f'reversed: {reversed_s}')
        for i in range(len(s)):
          if s[i] in map: 
            result+=reversed_s[0]
            reversed_s.pop(0)
            #print(f'reversed: {reversed_s}')    
          else:
            result+=s[i]
        return result
