class Solution:
    def encode(self, arr):
        # write your logic to encode the strings
        if not arr:
            return ""
        res = []
        for i in arr:
            res.append(len(i))
            res.extend(f"/:{i}")
            
        ret = "".join(str(x) for x in res)
        
        return ret
        
    def decode(self, s):
        if not s:
            return []
        
        i = 0
        res = []
        
        n = len(s)
        
        while i<n:
            gap_index = s.find("/:",i)
            
            length_word = int(s[i:gap_index])
            
            word_start = gap_index+2
            end = length_word+word_start
            
            res.append(s[word_start:end])
            
            i = end
        
        return res