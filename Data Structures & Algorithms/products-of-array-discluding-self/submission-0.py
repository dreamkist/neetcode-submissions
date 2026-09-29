class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n # if not pre assign [1,1,1,1,1] python will not know the index of the empty list it cannot create at the moment you can you append to do that that creates the index and value at the same time.
        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]
            
        right_product = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= right_product
            right_product *= nums[i]
            
        return ans




            