# Ajay Patel
# Assignment 7

import sys
import graph
import clique

filename = sys.argv[1]
infile = open(filename, "r")

clause = 1
my_list = []

for line in infile:
    index = 0
    while index < len(line):
        if line[index] == ")":
            clause += 1

        if (97 <= ord(line[index]) <= 122) or (ord(line[index]) == 126):
            if ord(line[index]) == 126:
                # print(line[index]+line[index+1], clause)
                my_list.append((line[index]+line[index+1], clause))
                index += 2
            else:
                # print(line[index], clause)
                my_list.append((line[index], clause))
                index += 1

        else:
            index += 1

infile.close()

# print(my_list)

sat_graph = graph.Graph(len(my_list))

for i in range(len(my_list)):
    for j in range(len(my_list)):

        # print(i, j)
        #WHERE THE CLAUSE NUMBER IS SAME
        if my_list[i][1] == my_list[j][1]:
            pass

        # WHERE THE 1st LITERAL CONTAINS ~
        elif len(my_list[i][0]) == 2:
            if len(my_list[j][0]) == 2:
                graph.add_edge(sat_graph, i, j)
            else:
                if ord(my_list[i][0][1]) == ord(my_list[j][0]):
                    pass
                else:
                    graph.add_edge(sat_graph, i, j)

        # WHERE THE 2nd LITERAL CONTAINS ~
        elif len(my_list[j][0]) == 2:
            if ord(my_list[i][0]) == ord(my_list[j][0][1]):
                # print(i, j)
                pass
            else:
                graph.add_edge(sat_graph, i, j)

        # EVERYTHING ELSE
        else:
            graph.add_edge(sat_graph, i, j)


# print(sat_graph.matrix)
solution = clique.k_clique(sat_graph, clause-1)
# print(clause-1)

# print(solution)

if solution is None:
    print("No satisfying assignments.")

else:
    if len(solution.matrix) == 1:
        print("Satisfying assignment:")
        print(my_list[0][0])

    else:
        extract_letters = []
        not_list = []
        for i in solution.matrix:
            if my_list[i][0].__contains__("~"):
                not_list.append(my_list[i][0].strip("~"))
            extract_letters.append(my_list[i][0].strip("~"))

        extract_letters.sort()
        # print(not_list)

        extract_letters_sorted = []
        for i in extract_letters:
            if i in not_list:
                extract_letters_sorted.append("~"+i)
            else:
                extract_letters_sorted.append(i)

        print("Satisfying assignment:")
        print(", ".join(extract_letters_sorted))