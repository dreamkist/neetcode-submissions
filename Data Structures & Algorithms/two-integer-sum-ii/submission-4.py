class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lennum = len(numbers)

        for i in range (lennum):
            low = i+1
            high = lennum-1

            while high >= low:

                mid = (low+high)//2

                if numbers[mid] == target-numbers[i]:
                    return [i+1,mid+1]
                elif numbers[mid] < target-numbers[i]:
                    low = mid + 1
                else:
                    high = mid - 1
                

