class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        sumset = {}
        i = 0

        while i<len(nums):
            diff = target-nums[i]

            if nums[i] in sumset:
                return[sumset[nums[i]], i]

            sumset[diff] = i
            i +=1
            