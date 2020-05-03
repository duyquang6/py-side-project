from typing import List


def recur(k, target, bl: set):
    if k == 1:
        if target not in bl and 1 <= target <= 9:
            return {(target,)}
        return {}
    res = set()
    for num in set(range(1, 10)) - bl:
        clone_bl = bl.copy()
        clone_bl.add(num)
        resp_set = recur(k - 1, target - num, clone_bl)
        if len(resp_set) == 0:
            continue
        res.update(tuple(sorted([num, *v])) for v in resp_set)

    return res


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return [list(val) for val in recur(k, n, {})]


print(Solution().combinationSum3(3, 27))
