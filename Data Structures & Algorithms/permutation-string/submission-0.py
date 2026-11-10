class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        
        hmcountmap = Counter(s1)

        for i in range (len(s2)-m+1):
            j = i+m
            h = s2[i:j]

            hmcounter2 = Counter(h)

            if (hmcountmap == hmcounter2):
                return True
        
        return False