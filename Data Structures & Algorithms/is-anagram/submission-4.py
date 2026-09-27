class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if (Counter(s) == Counter(t)):
        #     print (Counter(s))        yeh toh good tarika hai
        #     return True
        # return False
        c1 = dict()
        c2 = dict()
        for i in s:
            c1[i] = c1.get(i,0)+1
        for i in t:
            c2[i] = c2.get(i,0)+1
        if c1 == c2 :
            return True
        return False