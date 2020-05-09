class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return self.binarySearch(num, 0, num)

    def binarySearch(self, target, ss, se):
        if target == 0: return False
        mid = int((ss + se) / 2)
        sqr = mid * mid
        if ss < se:
            if sqr < target:
                return self.binarySearch(target, mid + 1, se)
            if sqr == target:
                return True
            return self.binarySearch(target, ss, mid - 1)
        return sqr == target
