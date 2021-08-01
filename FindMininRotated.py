#Space Complexity O(1)
#Time complexity O(Log N) where N is the number of elements in the array.

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = low + (high-low)//2
            if nums[low]<=nums[high]:
                return nums[low]
            if (mid == 0 or nums[mid]<nums[mid-1]) and (mid == len(nums)-1 or nums[mid]<nums[mid+1]):
                return nums[mid]
            if nums[low]<=nums[mid]:
                low = mid+1
            else:
                high = mid-1
        return