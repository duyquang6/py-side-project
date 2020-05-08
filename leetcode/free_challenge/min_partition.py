class Solution:
    def minPartitions(self, used: [int], total: [int]) -> int:
        res = sum(used)
        total.sort(reverse=True)
        for i, v in enumerate(total):
            res -= v
            if res <= 0:
                return i+1

        raise Exception('Over capacity')


print(Solution().minPartitions([3, 2, 1, 100, 1], [3, 5, 3, 5, 5]))
