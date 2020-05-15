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


def bellman_ford(edges, V, x):
    dist = [math.inf] * V
    dist[x] = 0
    for _ in range(V-1):
        for u, v, w in edges:
            dist[v] = min(dist[v], dist[u]+w)
    return dist


def detect_negative_cycle(edges, V, x):
    dist = [math.inf] * V
    dist[x] = 0
    for i in range(V):
        for u, v, w in edges:
            if i == V-1 and dist[v] > dist[u]+w:
                return True
            dist[v] = min(dist[v], dist[u]+w)
    return False


def convert_adj_to_edge_list(adj):
    V = len(adj)
    edge_list = []
    for u in range(V):
        # v is u neighbor
        for v, w in adj[u]:
            edge_list.append((u, v, w))
    return edge_list


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
    edge_list_form = convert_adj_to_edge_list(adj)
    print(bellman_ford(edge_list_form, V, 0))
    print(detect_negative_cycle(edge_list_form, V, 0))
