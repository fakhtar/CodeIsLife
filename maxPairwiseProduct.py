array = [20,1,4,2,6,7,8,1,1,23,4,7,8,100,100,28,4]

def find_max_pair(array):
    max1 = None
    max2 = None
    if array[0] == array[1]:
        max1 = array[0]
        max2 = array[0]
    elif array[0] > array[1]:
        max1 = array[1]
        max2 = array[0]
    elif array[0] < array[1]:
        max1 = array[0]
        max2 = array[1]
    len_of_arr = len(array)
    for i in range(2,len_of_arr):
        if array[i] == max2:
            max1 = array[i]
        elif array[i] > max2:
            max1 = max2
            max2 = array[i]
        elif array[i] < max2 and array[i] >= max1:
            max1 = array[i]

            
    return (max1,max2)

def find_max_pair_again(array):
    pair_arr = []
    for item in array:
        if len(pair_arr) < 2:
            pair_arr.append(item)
        elif item >= max(pair_arr) or item >= min(pair_arr):
            pair_arr.pop(pair_arr.index(min(pair_arr)))
            pair_arr.append(item)
    return pair_arr

        

print(find_max_pair(array))
print(find_max_pair_again(array))