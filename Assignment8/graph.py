# Ajay Patel
# Assignment 8

from collections import defaultdict

class Graph:

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = defaultdict(list)

    def add_edge(self, v1, v2):
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)

    def remove_edge(self, v1, v2):
        pass

    def is_empty(self):
        for i in self.graph:
            if len(self.graph[i]) > 0:
                return False
        return True

    def get_degrees(self):
        degrees = [0] * self.num_vertices
        for i in self.graph:
            degrees[i] = len(self.graph[i])

        return degrees




# # Represents an undirected, unweighted graph.
# # NOTE: Do not alter this file.
# # CSC 349, Assignment 7
# # Given code, Fall '19
#
#
# class Graph:
#     """ A collection of vertices connected by edges """
#
#     def __init__(self, num_vertices = 0):
#         # The backing adjacency dictionary:
#         self.matrix = {vertex: set() for vertex in range(num_vertices)}
#
#     def __eq__(self, other):
#         return type(other) == Graph and self.matrix == other.matrix
#
#     def __repr__(self):
#         return "Graph({\n    %s\n})" % ",\n    ".join(
#                 ["%s: %s" % (v, sorted(self[v])) for v in sorted(self)])
#
#     def __iter__(self):
#         return iter(self.matrix)
#
#     def __contains__(self, item):
#         return item in self.matrix
#
#     def __getitem__(self, key):
#         return self.matrix[key]
#
#     def __setitem__(self, key, value):
#         self.matrix[key] = value
#
#
# def add_vertex(graph, vertex):
#     """
#     Add a vertex to a graph, if it does not exist.
#     :param graph: The graph to which to add the vertex
#     :param vertex: The vertex to be added
#     :return: The vertex's adjacency set
#     """
#     return graph.matrix.setdefault(vertex, set())
#
#
# def add_edge(graph, vertex_u, vertex_v):
#     """
#     Add an edge to a graph, adding vertices first if they do not exist.
#     :param graph: The graph to which to add the edge
#     :param vertex_u: The edge's first endpoint
#     :param vertex_v: The edge's second endpoint
#     :return: The resulting graph
#     """
#     add_vertex(graph, vertex_u).add(vertex_v)
#     add_vertex(graph, vertex_v).add(vertex_u)
#     return graph
#
#
# def remove_edge(graph, vertex):
#     g = Graph()
#     for i in graph.matrix:
#         if i == vertex:
#             pass
#         else:
#             for j in graph.matrix[i]:
#                 if j == vertex:
#                     pass
#                 else:
#                     add_edge(g, i, j)
#     return g
#
#     # del graph[vertex_u]
#
#     # return graph
#         # for j in graph.matrix[i]:
#         #     if (i == vertex_u) and (j == vertex_v):
#         #         pass
#         #     elif (i == vertex_v) and (j == vertex_u):
#         #         pass
#         #     else:
#         #         add_edge(g , vertex_u, vertex_v)
#     return g
#
#
# def is_empty(graph):
#     for i in graph.matrix:
#         if len(graph.matrix[i]) > 0:
#             return False
#     return True
#
#
# def read_graph(graph_fname):
#     """
#     Read a graph from a file.
#     :param graph_fname: The name of a file containing an edge list
#     :return: The corresponding new graph
#     """
#     graph = Graph()
#     file = open(graph_fname, "r")
#
#     for line in file:
#         # print(line)
#         index = 0
#         vertex1 = ""
#         while line[index] != " ":
#             vertex1 += line[index]
#             index += 1
#
#         vertex2 = ""
#         index += 1
#         while index < len(line):
#             if line[index] == "\n":
#                 break
#             else:
#                 vertex2 += line[index]
#                 index += 1
#
#         vertex1 = int(vertex1.strip())
#         vertex2 = int(vertex2.strip())
#
#         add_edge(graph, vertex1, vertex2)
#
#     return graph
