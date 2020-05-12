class Solution:
    memo = {
        0: 0,
        1: 1,
        2: 1
    }

    def tribonacci(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]

        for i in range(1, 4, 1):
            if n-i not in self.memo:
                self.memo[n-i] = self.tribonacci(n-i)
            self.memo[n] = self.memo.get(n, 0) + self.memo[n-i]

        return self.memo[n]
