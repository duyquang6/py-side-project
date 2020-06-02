import itertools
from collections import deque
from functools import lru_cache
from typing import List


#
# class Solution:
#     # def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
#     #     preps = [set() for _ in range(n)]
#     #     reverse_preps = [set() for _ in range(n)]
#     #     for prep in prerequisites:
#     #         preps[prep[0]].add(prep[1])
#     #         for p in reverse_preps[prep[0]]:
#     #             preps[p].add(prep[1])
#     #             reverse_preps[prep[1]].add(p)
#     #         reverse_preps[prep[1]].add(prep[0])
#     #     return [query[1] in preps[query[0]] for query in queries]
#     def cherryPickup(self, grid: List[List[int]]) -> int:
#         m = len(grid);
#         n = len(grid[0]);
#
#         @lru_cache(None)
#         def dfs(r, c1, c2):
#             num_cherry = grid[r][c1] if c1 == c2 else grid[r][c1] + grid[r][c2]
#             if r == m-1:
#                 return num_cherry
#             ans = 0
#             for i in range(c1 - 1, c1 + 2):
#                 if 0 <= i < n:
#                     for j in range(c2 - 1, c2 + 2):
#                         if 0 <= j < n:
#                             ans = max(ans, dfs(r + 1, i, j))
#             return ans + num_cherry
#
#         return dfs(0, 0, n - 1)


class Solution:
    def getProbability(self, balls: List[int]) -> float:
        temp = []
        for c, b in enumerate(balls):
            for i in range(b):
                temp.append(c)
        n = len(temp)
        ans = 0
        omega = 0
        for c in itertools.permutations(temp, n // 2):
            omega += 1
            if all(c.count(k) != (balls[k] / 2) for k in set(c)):
                ans += 1
        return ans / omega


print(Solution().getProbability([1, 2, 1, 2]))
