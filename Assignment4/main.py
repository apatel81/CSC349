# Ajay Patel
# Assignment 4

from scc import *
import sys

vertex_list = []
filename = sys.argv[1]
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

    vertex1 = int(vertex1.strip())
    vertex2 = int(vertex2.strip())

    if vertex1 not in vertex_list:
        vertex_list.append(vertex1)

    if vertex2 not in vertex_list:
        vertex_list.append(vertex2)

file.close()


g = Graph(len(vertex_list))
file2 = open(filename, "r")

for line in file2:
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

    vertex1 = int(vertex1.strip())
    vertex2 = int(vertex2.strip())

    g.add_edge(vertex1, vertex2)

file2.close()

final_list = []
a = g.findCCs(final_list)
unique_list = []

for i in a:
    if i not in unique_list:
        unique_list.append(i)

for i in unique_list:
    i.sort()

print(len(unique_list), "Strongly Connected Component(s):")
for i in unique_list:
    print(*i, sep=", ")