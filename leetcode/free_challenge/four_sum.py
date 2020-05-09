from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in nums[:-3]:
            for j in nums[i+1:-2]:
                m, n = j+1, len(nums)-1
                while m < n:
                    s = i + j + nums[m]+nums[n]
                    if s == target:
                        res.append(i, j, nums[m], nums[n])
                        m+=1
                        n-=1

                    if s < target:
                        

        return res


print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
