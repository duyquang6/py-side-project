# # adjacency list using linkedlist standard
# # slow implementation
# class AdjacentNode:
#     def __init__(self, data):
#         self.vertex = data
#         self.next = None


# class Graph:
#     def __init__(self, num_vertices):
#         self.V = num_vertices
#         self.graph = [None] * self.V

#     def add_edge(self, src, dest):
#         dest_node = AdjacentNode(dest)
#         dest_node.next = self.graph[src]
#         self.graph[src] = dest_node

#         # Adding the source node to the destination as
#         # it is the undirected graph
#         node = AdjacentNode(src)
#         node.next = self.graph[dest]
#         self.graph[dest] = node

#     def print_graph(self):
#         for i in range(self.V):
#             print("Adjacency list of vertex {}\n head".format(i), end="")
#             temp = self.graph[i]
#             while temp:
#                 print(" -> {}".format(temp.vertex), end="")
#                 temp = temp.next
#             print(" \n")


# # Driver program to the above graph class
# if __name__ == "__main__":
#     V = 5
#     graph = Graph(V)
#     graph.add_edge(0, 1)
#     graph.add_edge(0, 4)
#     graph.add_edge(1, 2)
#     graph.add_edge(1, 3)
#     graph.add_edge(1, 4)
#     graph.add_edge(2, 3)
#     graph.add_edge(3, 4)

#     graph.print_graph()

import pprint


def add_edge(adj: [[int]], u: int, v: int):
    adj[u].append(v)
    adj[v].append(u)
    return u


def dfs(adj: [[int]], V: int):
    visited = [False] * V
    for i in range(V):
        if not visited[i]:
            dfs_util(i, adj, visited)


def dfs_util(u: int, adj, visited):
    visited[u] = True
    print(" ", u)
    for i in range(len(adj[u])):
        if not visited[adj[u][i]]:
            dfs_util(adj[u][i], adj, visited)


def convert_adj_list_to_adj_matrix(adj):
    V = len(adj)
    adj_matrix = [[0]*V for _ in range(V)]
    for u in range(len(adj)):
        # v is u neighbor
        for v in adj[u]:
            adj_matrix[u][v] = 1

    return adj_matrix


def convert_adj_matrix_to_adj_list(adj_matrix):
    V = len(adj_matrix)
    adj = [[] for i in range(V)]
    for u in range(V):
        for v in range(V):
            if adj_matrix[u][v] == 1:
                adj[u].append(v)
    return adj


def convert_adj_to_edge_list(adj):
    V = len(adj)
    edge_list = []
    for u in range(len(adj)):
        # v is u neighbor
        for v in adj[u]:
            edge_list.append((u, v))
    return edge_list


if __name__ == "__main__":
    V = 5
    adj = [[] for i in range(V)]
    add_edge(adj, 0, 1)
    add_edge(adj, 0, 4)
    add_edge(adj, 1, 2)
    add_edge(adj, 1, 3)
    add_edge(adj, 1, 4)
    add_edge(adj, 2, 3)
    add_edge(adj, 3, 4)
    dfs(adj, V)

    adj_matrix = convert_adj_list_to_adj_matrix(adj)
    pprint.pprint(adj_matrix)
    new_adj = convert_adj_matrix_to_adj_list(adj_matrix)
    dfs(adj, V)
    new_adj_matrix = convert_adj_list_to_adj_matrix(adj)
    pprint.pprint(new_adj_matrix)

    edge_list = convert_adj_to_edge_list(adj)
    print(edge_list)
