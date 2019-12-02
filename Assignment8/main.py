from graph import *
import cover
import sys

vertex_list = []
filename = sys.argv[1]
file1 = open(filename, "r")

for line in file1:
    index = 0
    vertex1 = ""
    while line[index] != " ":
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

    vertex1 = int(vertex1.strip())
    vertex2 = int(vertex2.strip())

    if vertex1 not in vertex_list:
        vertex_list.append(vertex1)

    if vertex2 not in vertex_list:
        vertex_list.append(vertex2)

file1.close()

g1 = Graph(len(vertex_list))
g2 = Graph(len(vertex_list))
g3 = Graph(len(vertex_list))
file2 = open(filename, "r")

for line in file2:
    index = 0
    vertex1 = ""
    while line[index] != " ":
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

    vertex1 = int(vertex1.strip())
    vertex2 = int(vertex2.strip())

    g1.add_edge(vertex1, vertex2)
    g2.add_edge(vertex1, vertex2)
    g3.add_edge(vertex1, vertex2)

file2.close()

# print(g.graph)
# for i in g.graph:
#     print(i, g.graph[i])


smart = cover.SmartGreedyVC(g1)
approx = cover.approximation(g2)
brute = cover.brute(g3)

brute.sort()

# print("log-Approximation:", *smart)
# print("2-Approximation:", *approx)
# print("Exact Solution:", *brute)

with open('my1.txt', 'w') as f:
    f.write("log-Approximation: ")
    for i in smart:
        f.write("%s " % i)

    f.write("\n")
    f.write("2-Approximation: ")
    for i in approx:
        f.write("%s " % i)

    f.write("\n")
    f.write("Exact Solution: ")
    for i in brute:
        f.write("%s " % i)
