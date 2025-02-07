class Solution:
    def groupAnagrams(self, s: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for i in s:
            arr = [0] * 26
            for c in i:
                arr[ord(c) - ord('a')]+=1
            result[tuple(arr)].append(i)
        return list(result.values())
