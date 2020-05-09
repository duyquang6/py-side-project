# Geotech
# Problem: https://scontent-hkt1-1.xx.fbcdn.net/v/t1.15752-9/95656932_2490306151186044_7724774758058819584_n.jpg?_nc_cat=100&_nc_sid=b96e70&_nc_oc=AQnZHlB8vgybXDSsik320OhtsL-v-gNICMXqrWPvWSKR3f9vpxTy5TQc1znI5mf3qJ0&_nc_ht=scontent-hkt1-1.xx&oh=d9ceac33031b17abe8da9c13380cfdae&oe=5ED9B8AE

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
