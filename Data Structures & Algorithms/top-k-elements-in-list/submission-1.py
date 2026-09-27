class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c1 = Counter(nums)
        lit = sorted(c1, key = c1.get, reverse=True)
        return lit[:k]