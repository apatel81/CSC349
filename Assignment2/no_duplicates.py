#CSC 349 - Assignment 1
#Name: Ajay Patel

new_list = []
def remove_duplicates(lst1, min, max):
    mid = (min+max)//2
    if len(lst1) == 1:
        return lst1[0]

    elif (lst1[mid-1] != lst1[mid]) and (lst1[mid+1] != lst1[mid]):
        return lst1[mid]

    elif mid%2 == 0:
        if lst1[mid+1] == lst1[mid]:
            return remove_duplicates(lst1, mid, max)

        elif lst1[mid-1] == lst1[mid]:
            return remove_duplicates(lst1, min, mid)
    elif mid%2 == 1:
        if lst1[mid+1] == lst1[mid]:
            return remove_duplicates(lst1, min, mid-1)

        elif lst1[mid-1] == lst1[mid]:
            return remove_duplicates(lst1, mid+1, max)


    #THIS IS THE CODE FOR NUMBER 7
    # if left[i] != right[j]:
    #     if left[i] not in new_list:
    #         new_list.append(left[i])
    #     if right[j] not in new_list:
    #         new_list.append(right[j])
    #     i += 1
    #     j += 1
    #
    # else:
    #     j += 1
    #
    # print(left, right, "--->", new_list)

