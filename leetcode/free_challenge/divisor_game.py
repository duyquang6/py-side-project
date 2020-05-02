class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = [None, False, True]
        if N <= 2:
            return dp[N]
        for i in range(3, N+1):
            dp.append(False)
            for k in range(1, int(N/2)+1):
                if i % k == 0 and dp[k]:
                    dp[i] = True
                    break
        return dp[N]


print(Solution().divisorGame(5))
