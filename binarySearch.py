A = [1,2,3,4,5]

# def binary_search(my_list, val):
#     len_list = len(my_list)
#     if len_list == 1:
#         return my_list[0] == val 
#     else:
#         if len_list % 2 == 0:
#             len_div_2 = int(len_list/2)
#             return binary_search(my_list[0:len_div_2], val) or binary_search(my_list[len_div_2:len_list], val)
#         else:
#             len_div_2 = int(round(len_list/2))
#             return binary_search(my_list[0:len_div_2], val) or binary_search(my_list[len_div_2:len_list], val)


# def binary_search(my_list, val):
#     len_list = len(my_list)
#     if len_list == 1:
#         return my_list[0] == val 
#     else:
#         len_div_2 = int(round(len_list/2))
#         return binary_search(my_list[0:len_div_2], val) or binary_search(my_list[len_div_2:len_list], val)

def binary_search(my_list, val, start):
    len_list = len(my_list)
    if len_list == 0:
        return -1
    len_div_2 = int(round(len_list/2))
    if my_list[len_div_2] == val:
        return  len_div_2 + start
    elif my_list[len_div_2] < val:
        return binary_search(my_list[len_div_2+1:], val, len_div_2+1)
    else:
        return binary_search(my_list[:len_div_2], val, start)
for item in A:
    print(binary_search(A,item,0))