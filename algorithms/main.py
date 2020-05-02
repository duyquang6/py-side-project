

class UnionFind():
    def __init__(self):
        self._id = list(range(n))

    def connected(self, p: int, q: int) -> bool:
        return self._id[p] == self._id[q]

    def union(self, p, q):
        pid, qid = self._id[p], self._id[q]
        for idx, val in enumerate(self._id):
            if val == pid:
                self._id[idx] = qid
