class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minstr = min(strs)
        counter = 0
        temp = ''
        for i in range(len(minstr)):
            if counter == len(strs):
                return temp
            temp = minstr[:len(minstr)-i]

            for s in strs:
                index = s.find(temp)
                if index == 0:
                    counter+=1
                else:
                    counter = 0
                    break     
        if counter == len(strs):
            return temp
        return ''
