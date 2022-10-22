# Problem - 1


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            
            midIndex = (low + high) // 2
            
            if nums[midIndex] == target:
                return midIndex
            
            elif nums[midIndex] > target:
                high = midIndex - 1
                
            else:
                low = midIndex + 1
                
        return -1


Solution()