from typing import List


class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        return self.shopping(price, special, needs)

    def shopping(self, prices: [int], specials: [[int]], needs: [int]):
        if all(need == 0 for need in needs):
            return 0
        res = 0
        for i, price in enumerate(prices):
            res += needs[i] * price

        for offer in specials:
            # check if offer can apply
            clone_needs = [needs[i] - quantity for i, quantity in enumerate(offer[:-1])]
            if any(val < 0 for val in clone_needs):
                continue
            clone_res = self.shopping(prices, specials, clone_needs) + offer[-1]
            if clone_res < res:
                res = clone_res

        return res


print(Solution().shoppingOffers([2, 3, 4], [[1, 1, 0, 4], [2, 2, 1, 9]], [1, 2, 1]))
