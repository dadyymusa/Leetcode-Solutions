class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # index of the maximum number 
        hi = len(nums) - 1
        # index of the lowest number 
        lo = 0

        while hi >= lo:
            mid = (hi + lo) // 2

            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                hi = mid - 1 
            else:
                lo = mid + 1
        
        return -1