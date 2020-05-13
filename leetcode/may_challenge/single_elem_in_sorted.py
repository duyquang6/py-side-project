class Solution:
    def singleNonDuplicate(self, nums: [int]) -> int:
        if len(nums) == 1:
            return nums[0]
        ss, se = 0, len(nums)-1
        while ss < se:
            mid = int((se + ss) / 2)
            val = nums[mid]
            if mid > 0 and mid < len(nums)-1 and nums[mid-1] < val and val < nums[mid+1]:
                return val
            if (mid == 0 and nums[mid+1] > val) or (mid == len(nums)-1 and nums[mid-1] < val):
                return val

            if mid % 2 != 0:
                if val == nums[mid-1]:
                    ss = mid+1
                elif val == nums[mid+1]:
                    se = mid-1
            if mid % 2 == 0:
                if val == nums[mid-1]:
                    se = mid - 1
                elif val == nums[mid+1]:
                    ss = mid+1
        return nums[ss]


print(Solution().singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
