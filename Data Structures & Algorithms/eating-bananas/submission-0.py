class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        sortpile = piles
        n = len(piles)

        low = 1
        high = max(piles)
        ans = high

        while low <= high:
            mid = low + (high - low) // 2

            tempadd = 0
            for i in range(n):
                tempadd = tempadd + math.ceil(sortpile[i] / mid)

            if tempadd > h:
                low = mid + 1
            else:
                ans = mid
                high = mid - 1

        return ans