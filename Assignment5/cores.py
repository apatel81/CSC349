# Ajay Patel
# Assignment 5


from collections import defaultdict


class Graph:


    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = defaultdict(list)


    def add_edge(self, v1, v2):
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)


    def updateDegrees(self, vertex, degrees, k):
        if degrees[vertex] < k:
            for i in self.graph[vertex]:
                degrees[i] -= 1


    def findCores(self, k, final_list):
        temp_list= []
        degrees = [0] * self.num_vertices

        for i in self.graph:
            degrees[i] = len(self.graph[i])

        for v in range(self.num_vertices):
            self.updateDegrees(v, degrees, k)

        for v in range(self.num_vertices):
            if degrees[v] >= k:
                temp_list.append(v)

        final_list.append(temp_list)

        return final_list