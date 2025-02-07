class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nmap1 = {}
        nmap2 = {}
        
        for i in nums1:
            nmap1[i] = nmap1.get(i, 0) + 1
        for i in nums2:
            nmap2[i] = nmap2.get(i, 0) + 1
        
        temp = []
        result = []
        if len(nums1) > len(nums2):
            temp = nums1
        else:
            temp = nums2
        
        for i in temp:
            if i in nmap1 and i in nmap2:
                result.append(i)
                if nmap1[i] <= 1:
                    del nmap1[i]
                else:
                    nmap1[i]-=1
                if nmap2[i] <= 1:
                    del nmap2[i]
                else:
                    nmap2[i]-=1
        return result
