# dijkstra using adjancent list because it loop through vertex and determine final cost on that each vertex


import math
import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def is_empty(self):
        return not len(self._queue)


def dijkstra(adj, x):
    # adj: adjacent list of graph
    # x: start node
    pq = PriorityQueue()
    V = len(adj)
    distance = [math.inf]*V
    distance[x] = 0
    pq.push(x, 0)
    while not pq.is_empty():
        a = pq.pop()
        for u in adj[a]:
            b, w = u
            if distance[a] + w < distance[b]:
                distance[b] = distance[a] + w
                pq.push(b, -distance[b])
    return distance


def add_edge(adj: [[int]], u: int, v: int, w: int):
    adj[u].append((v, w))
    adj[v].append((u, w))
    return u


if __name__ == "__main__":
    V = 5
    adj = [[] for i in range(V)]
    add_edge(adj, 0, 3, 9)
    add_edge(adj, 0, 4, 1)
    add_edge(adj, 0, 1, 5)
    add_edge(adj, 4, 3, 2)
    add_edge(adj, 2, 3, 6)
    add_edge(adj, 1, 2, 2)

    print(dijkstra(adj,0))
