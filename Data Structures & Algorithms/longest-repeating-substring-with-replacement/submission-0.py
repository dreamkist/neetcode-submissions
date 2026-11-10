class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        hm = {}
        res = 0
        l = 0

        for i in range (len(s)):

            hm[s[i]]  = hm.get(s[i],0)+1

            if (sum(hm.values())-max(hm.values())) > k:
                hm[s[l]] -= 1
                l +=1
            

            res = max(res,sum(hm.values()))
        
        return res