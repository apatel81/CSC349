# Ajay Patel
# Assignment 3

from bicolor import *
import sys


seen = []
output = []
g = Graph(sys.argv[1])

if g.bicolor() == True:
    for i in g.vertlist:
        i.adjacent_to.sort()
    print("Is 2-colorable:")
    for i in g.vertlist:
        for j in g.vertlist:
            if (i.id != j.id) and (i.adjacent_to == j.adjacent_to) and (j.id not in seen):
                seen.append(j.id)
                seen.append(i.id)
                output.append(i.adjacent_to)
        # print(i.id, " ", i.adjacent_to)
        if len(i.adjacent_to) == 1:
            output.append(i.adjacent_to)

    final = []
    compare = []
    for i in output:
        compare.append(i[0])

    compare.sort()
    for i in compare:
        for j in output:
            if i == j[0]:
                final.append(j)

    for i in final:
        print(*i, sep = ", ")

else:
    print("Is not 2-colorable.")

