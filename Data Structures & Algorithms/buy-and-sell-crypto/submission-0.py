class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min = 999999
        

        for i in prices:
            
            if i <= min :
                min = i
            
            if (i-min)>= res:
                res = i-min
        
        return res
            