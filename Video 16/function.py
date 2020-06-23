def find_max(find_max_of):
    max = 0
    for item in find_max_of:
        if item > max:
            max = item
    return max
print(find_max([0,2,11,4,6,7,8,9]))
print(find_max([0,2,111,4,6,7,8,219]))