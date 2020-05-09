
class Solution:
    def mySqrt(self, x: int) -> int:
        return self.binarySearch(x, 0, x)

    def binarySearch(self, target, ss, se):
        if ss < se:
            mid = int((ss + se)/2)
            sqr = mid ** 2
            if sqr == target:
                return mid
            if sqr < target:
                return self.binarySearch(target, mid+1, se)
            return self.binarySearch(target, ss, mid-1)

        return ss-1 if ss ** 2 > target else ss


print(Solution().mySqrt(4))
print(Solution().mySqrt(8))
