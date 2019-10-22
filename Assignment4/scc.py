# Ajay Patel
# Assignment 4

from collections import defaultdict


class Vertex:
    def __init__(self, id, visited):
        self.id = id
        self.visited = False


class Graph:


    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = defaultdict(list)


    def add_edge(self, v1, v2):
        self.graph[v1].append(v2)


    def explore(self, vertex, visited, final_list, temp_list):
        visited[vertex] = True
        temp_list.append(vertex)

        for i in self.graph[vertex]:
            if visited[i] == False:
                self.explore(i, visited, final_list, temp_list)

        final_list.append(temp_list)


    def fillStack(self, vertex, stack, visited):
        visited[vertex] = True

        for i in self.graph[vertex]:
            if visited[i] == False:
                self.fillStack(i, stack, visited)

        stack.append(vertex)


    def getTranspose(self):
        g = Graph(self.num_vertices)

        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)

        return g


    def findCCs(self, final_list):
        stack = []
        visited = [False] * self.num_vertices

        for i in range(self.num_vertices):
            if visited[i] == False:
                self.fillStack(i, stack, visited)

        reversed_graph = self.getTranspose()
        visited = [False] * self.num_vertices

        while stack:
            i = stack.pop()
            if visited[i] == False:
                temp_list = []
                reversed_graph.explore(i, visited, final_list, temp_list)

        return final_list