class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        hm = {}
        l = 0
        right = 0
        res = 0



        for i in range(len(s)):
            if s[i] in hm:
                if hm[s[i]] >= l:
                    l = hm[s[i]]+1
            
            hm[s[i]] = i

            res = max(res,i-l+1)
        
        return res