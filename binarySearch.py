A = [1,4,7,6,3,9]

def binary_search(my_list, val):
    len_list = len(my_list)
    if len_list == 1:
        return my_list[0] == val 
    else:
        if len_list % 2 == 0:
            len_div_2 = int(len_list/2)
            return binary_search(my_list[0:len_div_2], val) or binary_search(my_list[len_div_2:len_list], val)
        else:
            len_div_2 = int(round(len_list/2))
            return binary_search(my_list[0:len_div_2], val) or binary_search(my_list[len_div_2:len_list], val)

print(binary_search(A,9))