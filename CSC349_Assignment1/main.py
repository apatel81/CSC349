#CSC 349 - Assignment 1
#Name: Ajay Patel


import random
import unittest
import sys
from sorting_algorithms import *

my_list = []
with open(sys.argv[1], 'r') as my_file:
    my_file = my_file.read()
    my_file = my_file.split(", ")
    for i in my_file:
        my_list.append(int(i))

# print(my_list)

selection_list = selection_sort(my_list)
insertion_list = insertion_sort(my_list)
merge_list = merge_sort(my_list)

selection_list = [str(i) for i in selection_list]
selection_list = ", ".join(selection_list)
# f = open("my_output.txt", 'w')
# f.write("Selection Sort: ")
# f.write(selection_list)
# f.write("\n")

print("Selection Sort: " + selection_list)

insertion_list = [str(i) for i in insertion_list]
insertion_list = ", ".join(insertion_list)
# f.write("Insertion Sort: ")
# f.write(insertion_list)
# f.write("\n")

print("Insertion Sort: " + insertion_list)

merge_list = [str(i) for i in merge_list]
merge_list = ", ".join(merge_list)
# f.write("Merge Sort    : ")
# f.write(merge_list)
# f.write("\n")

print("Merge Sort:     " + merge_list)

# f.close()

# if __name__ == '__main__':
#     unittest.main()