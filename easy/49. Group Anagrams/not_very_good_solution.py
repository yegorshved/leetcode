class Solution:
    def groupAnagrams(self, s: List[str]) -> List[List[str]]:
        
        result = defaultdict(list)

        for i in s:
            sortedS = ''.join(sorted(i))
            result[sortedS].append(i)
        
        return list(result.values())    
