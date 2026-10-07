class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        low = 0
        high = n-1
        temp1 = 0

        while low<high:
            if heights[low]>=heights[high]:
                if temp1 <= heights[high]*(high-low):
                    temp1 = heights[high]*(high-low)
                high = high-1
            if heights[high]>heights[low]:
                if temp1 <= heights[low]*(high-low):
                    temp1 = heights[low]*(high-low)
                low = low+1
        
        return temp1
                  
