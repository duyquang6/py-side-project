class Solution:
    def singleNonDuplicate(self, nums: [int]) -> int:
        if len(nums) == 1:
            return nums[0]
        ss, se = 0, len(nums)-1
        while ss < se:
            mid = (se + ss) / 2
            val = nums[mid]
            if mid > 0 and mid < len(nums)-1 and nums[mid-1] < val < nums[mid+1]:
                return val
            if mid == 0 and nums[mid+1] > val:
                return val
            if mid == len(nums)-1 and nums[mid-1] < val:
                return val
            


Solution().singleNonDuplicate([3, 3, 7, 7, 10, 11, 11])
