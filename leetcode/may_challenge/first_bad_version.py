def isBadVersion(n):
    if n < 2:
        return False
    return True


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        ss, se = 1, n
        while ss < se:
            mid = int((ss + se) / 2)
            if isBadVersion(mid):
                se = mid
            else:
                ss = mid + 1
        return int((ss + se) / 2)


print(Solution().firstBadVersion(2))
