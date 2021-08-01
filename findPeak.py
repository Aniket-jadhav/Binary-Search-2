#Space Complexity O(1)
#Time Complexity O(Log N) where N is the number of elements in the given array

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        while (low<=high):
            mid = low + (high-low)//2
            if (mid == 0 or nums[mid]>nums[mid-1]) and (mid == len(nums)-1 or nums[mid]>nums[mid+1]):
                return mid
            if mid!=0 and nums[mid-1]>nums[mid]:
                high = mid-1
            else:
                low = mid+1
        return