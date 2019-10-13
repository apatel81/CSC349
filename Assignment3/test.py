# Ajay Patel
# Assignment 3

from queueArray import *


class Vertex:
    def __init__(self, key, discovered):
        self.id = key
        self.discovered = False
        self.adjacent_to = []

    def add_neighbor(self, v):
        self.adjacent_to.append(v.id)

    def getConnection(self):
        return self.adjacent_to


class Graph:
    def __init__(self, filename):
        self.vertlist = []
        self.number_of_vertices = 0

        file = open(filename, "r")
        for line in file:
            index = 0
            vertex1 = ""
            while line[index] != ",":
                vertex1 += line[index]
                index += 1

            vertex2 = ""
            index += 1
            while index < len(line):
                if line[index] == "\n":
                    break
                else:
                    vertex2 += line[index]
                    index += 1

            vertex1 = vertex1.strip()
            vertex2 = vertex2.strip()
            # print(vertex1)
            # print(vertex2)
            vertex1 = self.make_vertex(vertex1)  # Now a vertex object
            vertex2 = self.make_vertex(vertex2)  # Now a vertex object
            #print(vertex1.id, vertex2.id)
            self.add_edge(vertex1.id, vertex2.id)

        file.close()

    # Add Vertex object to list of vertices
    def add_vertex(self, id):
        self.number_of_vertices += 1
        self.vertlist.append(self.make_vertex(id))

    # Takes numbers from input statement and creates Vertex object
    def make_vertex(self, key):
        return Vertex(key, False)

    # Creates edge between 2 vertices
    def add_edge(self, v1, v2):
        if not self.is_in(v1, self.vertlist):
            self.add_vertex(v1)
        if not self.is_in(v2, self.vertlist):
            self.add_vertex(v2)

        # a and b are vertex objects
        a = self.find_vertex(v1, self.vertlist)
        b = self.find_vertex(v2, self.vertlist)

        a.add_neighbor(b)
        b.add_neighbor(a)

    def find_vertex(self, key, alist):
        for v in alist:
            if v.id == key:
                return v

    def is_in(self, key, alist):
        for v in alist:
            if v.id == key:
                return True
        return False

    def bicolor(self):
        # visited_list = []
        A = []
        B = []
        my_queue = QueueArray(100)
        bipartite = True
        while bipartite:
            for v in self.vertlist:   #vertlist is list of all vertices
                # if v.id not in visited_list:    #if vertex has not been discovered
                if v.discovered == False:
                    # visited_list.append(v.id)   #add vertex to discovered list
                    v.discovered = True
                    A.append(v.id)              #A = list of vertices we traverse through
                    for i in v.getConnection():         #Get the neighbors of current vertex
                        # if i not in visited_list:       #If the neighbors of current vertex have not discovered
                        vrtx = self.find_vertex(i, self.vertlist)  # returns the vertex object of each neighbor
                        if vrtx.discovered == False:
                            # visited_list.append(i)      #Make the neighbors discovered
                            vrtx.discovered = True
                            B.append(i)                 #Add undiscovered neighbors of current vertex to B
                        my_queue.enqueue(vrtx)              #Add all neighbors of current vertex to queue
                    bipartite = self.bfs(my_queue, B) #Check if queue and B has a back edge
            print("A: ", A)
            print("B: ", B)
            break


        if bipartite:
            return True
        else:
            return False

    def bfs(self, q, alist):
        while q.is_empty() is False:
            tmp = q.dequeue()
            for i in tmp.getConnection():
                if i in alist:
                    return False
        return True
