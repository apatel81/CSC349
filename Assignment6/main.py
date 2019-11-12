# Ajay Patel
# Assignment 6

from dynamic import *
import sys

filename = sys.argv[1]
file = open(filename, "r")

linenum = 0
scoring_matrix = []

for line in file:
    index = 0
    if linenum == 0:
        string1 = ""
        while index < len(line):
            if line[index] == "\n":
                break
            else:
                string1 += line[index]
                index += 1

    elif linenum == 1:
        string2 = ""
        while index < len(line):
            if line[index] == "\n":
                break
            else:
                string2 += line[index]
                index += 1

    elif linenum > 2:
        input = line.split()[1:]
        temp = []
        for i in input:
            temp.append(int(i))
        scoring_matrix.append(temp)

    linenum += 1

file.close()


aligner = AlignmentFinder(string2, string1, scoring_matrix)
pairs = aligner.find_global_alignment()
aligner.print_sequences(pairs)
