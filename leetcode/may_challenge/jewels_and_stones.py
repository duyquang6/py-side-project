class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        j_set = set(w for w in J)
        for s in S:
            if s in j_set:
                count += 1
        return count

    # pythonista version
    def numJewelsInStones2(self, J, S):
        return sum(map(lambda s: J.count(s), S))


print(Solution().numJewelsInStones2("aA", "aAAbbbb"))
