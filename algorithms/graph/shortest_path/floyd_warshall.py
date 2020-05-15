# floyd-warshall using adjancent matrix to find shortest path between any two node
import math
import pprint

def floyd_warshall(adj_matrix):
    V = len(adj_matrix)
    dist = [[math.inf] * V for _ in range(V)]
    for i in range(V):
        for j in range(V):
            if adj_matrix[i][j]:
                dist[i][j] = adj_matrix[i][j]
            elif i == j:
                dist[i][j] = 0

    for v in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][v] + dist[v][j], dist[i][j])
    return dist


def convert_adj_list_to_adj_matrix(adj):
    V = len(adj)
    adj_matrix = [[0]*V for _ in range(V)]
    for u in range(len(adj)):
        # v is u neighbor
        for v,w in adj[u]:
            adj_matrix[u][v] = w

    return adj_matrix


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

    adj_matrix = convert_adj_list_to_adj_matrix(adj)
    pprint.pprint(floyd_warshall(adj_matrix))
