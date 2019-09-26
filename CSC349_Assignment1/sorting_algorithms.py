#CSC 349 - Assignment 1
#Name: Ajay Patel

import time
import random
import copy


def insertion_sort(lst1):
    start_time = time.time()
    lst2 = copy.copy(lst1)
    size = len(lst2)
    count = 0

    for i in range(1,size):
        current_value = lst2[i]
        position = i
        while position > 0 and lst2[position - 1] > current_value:
            lst2[position] = lst2[position - 1]
            count += 1
            position -= 1
        lst2[position] = current_value

    end_time = time.time()
    sort_time = end_time - start_time

    return lst2


def selection_sort(lst1):
    start_time = time.time()
    count = 0
    for i in range(len(lst1)):
        min_idx = i
        for k in range(i+1, len(lst1)):
            if lst1[k] < lst1[min_idx]:
                count += 1
                min_idx = k
        swap(lst1, min_idx, i)
    end_time = time.time()
    sort_time = end_time - start_time

    return lst1


def swap(A, x, y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp


def merge_sort(lst1):
    start_time = time.time()
    count = 0
    if len(lst1) > 1:
        count += 1
        mid = len(lst1)//2
        left = lst1[:mid]
        right = lst1[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k= 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                count += 1
                lst1[k] = left[i]
                i += 1
            else:
                count += 1
                lst1[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            count += 1
            lst1[k] = left[i]
            i += 1
            j += 1

        while j < len(right):
            count += 1
            lst1[k] = right[j]
            j += 1
            k += 1

        end_time = time.time()
        sort_time = end_time - start_time

        return lst1
