#Space Complexity O(1)
#Time Complexity O(Log N) where N is number of elements in the array.

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def leftmostElement(nums,target):
            low = 0
            high = len(nums)-1
            while low<=high:
                mid = low + (high-low)//2
                if nums[mid]==target:
                    if mid==0 or nums[mid-1]!=nums[mid]:
                        return mid
                    if nums[mid-1]==nums[mid]:
                        high = mid-1
                        continue
                if nums[mid]>target:
                    high = mid-1
                else:
                    low = mid+1
            return -1
        def righmostElement(nums,target):
            low = 0
            high = len(nums)-1
            while low<=high:
                mid = low + (high-low)//2
                if nums[mid]==target:
                    if mid==len(nums)-1 or nums[mid+1]!=nums[mid]:
                        return mid
                    if nums[mid+1]==nums[mid]:
                        low = mid+1
                        continue
                if nums[mid]>target:
                    high = mid-1
                else:
                    low = mid+1
                
            return -1
        left = leftmostElement(nums,target)
        if left == -1:
            return [-1,-1]
        right = righmostElement(nums,target)
        return [left,right]
        
        