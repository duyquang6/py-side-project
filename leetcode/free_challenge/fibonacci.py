# test yield

class Solution:
    def fibo(self, N):
        if N == 1 or N == 2:
            return 1
        first = self.fibo(N-1)
        second = self.fibo(N-2)
        yield first + second



test = Solution().fibo(3)

next(test)
