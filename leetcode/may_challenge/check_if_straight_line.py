from typing import List
import sys


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        k = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0]) if (coordinates[1][0] -
                                                                                                  coordinates[0][
                                                                                                      0]) != 0 else sys.maxsize
        return False if any(
            (coordinates[i + 1][0] - coordinates[i][0] == 0 and k != sys.maxsize) or (
                        coordinates[i + 1][0] - coordinates[i][0] != 0 and
                        (coordinates[i + 1][1] - coordinates[i][1]) / (coordinates[i + 1][0] - coordinates[i][0]) != k)
            for i in
            range(len(coordinates) - 1)) else True


print(Solution().checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
