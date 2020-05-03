class Solution:
    def findTargetSumWays(self, nums: [int], S: int) -> int:
        dp = [[0] * 2001 for _ in nums]
        print(dp[0][996])
        dp[0][nums[0] + 1000] = 1
        dp[0][-nums[0] + 1000] += 1
        for i, num in enumerate(nums[1:], 1):
            for s in range(-1000, 1001):
                if dp[i-1][s + 1000] > 0:
                    dp[i][s + num + 1000] += dp[i-1][s + 1000]
                    dp[i][s - num + 1000] += dp[i-1][s + 1000]
        return dp[len(nums)-1][S+1000]


print(Solution().findTargetSumWays([2,1,1,2], 0))
