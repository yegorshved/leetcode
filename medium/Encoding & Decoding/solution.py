from typing import List
from collections import defaultdict
class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for i in strs:
            result+=str(len(i)) + '#' + i
        print(result)
        return result
        
    def decode(self, s: str) -> List[str]:
        
        result = []
        i = 0
        while i < len(s):
            char = s[i]
            
            if char.isdigit():
               # 4#neet4#code4#love3#you
               # 4 - prefix_number
               # if we have a prefix number that takes space more than one char e.g. 10 or 100
               # for that case we need another loop
                prefix_number = char
                temp_iterator = i + 1
                while s[temp_iterator].isdigit():
                    prefix_number+=s[temp_iterator]
                    temp_iterator+=1                              
                num_length = int(prefix_number)
                
                start = i + len('#') + len(prefix_number)
                end = num_length + i + len('#') + len(prefix_number)
                
                result.append(s[start:end])
                i += num_length+1+len(prefix_number)
                
        
        return result
    
s = Solution()
#print(s.encode(["we","say",":","yes","!@#$%^&*()"]))
print(s.decode('10#!@#$%^&*()'))
t = '4#neet4#code4#love3#you'
print(t[2:4+2])
