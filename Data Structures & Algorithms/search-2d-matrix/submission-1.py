class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        m = len(matrix)
        n = len(matrix[0])
        
        low = 0
        high = (m * n) - 1
        
        while high >= low:
            mid = high+low // 2
            midrow = mid // n
            midcol = mid % n
            
            if matrix[midrow][midcol] == target:
                return True
                
            if matrix[midrow][midcol] < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return False