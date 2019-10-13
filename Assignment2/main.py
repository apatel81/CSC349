#CSC 349 - Assignment 1
#Name: Ajay Patel

import sys
from no_duplicates import *

my_list = []
with open(sys.argv[1], 'r') as my_file:
    my_file = my_file.read()
    my_file = my_file.split(", ")
    for i in my_file:
        my_list.append(int(i))

merge_list = remove_duplicates(my_list, 0, len(my_list)-1)

print(merge_list)
