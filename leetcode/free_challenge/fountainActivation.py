# Geotech
# Problem: https://scontent-hkt1-1.xx.fbcdn.net/v/t1.15752-9/96596133_253938615726473_1335414939891793920_n.jpg?_nc_cat=110&_nc_sid=b96e70&_nc_oc=AQm0TOYT7Hz-dRjQOzb2r5XRMqcHVWwLpwy8b5gnPxgMoK91ZKukxXxxknuEHGaH1FM&_nc_ht=scontent-hkt1-1.xx&oh=bbbb5e2964f192753c43264278daed4b&oe=5EDA00FF


class Solution:
    def fountainActivation(self, locations: [int]) -> int:
        n = len(locations)
        fountains_range = []
        for i, loc in enumerate(locations):
            fountains_range.append([max(i+1 - loc, 1), min(i+1 + loc, n)])
        dp = []
        for i, rang in enumerate(fountains_range):
            dp.append()
        return dp


print(Solution().fountainActivation([1, 2, 1]))
