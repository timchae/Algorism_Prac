input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    max1 = 0
    for inpu in array:
        b = inpu
        if b > max1:
            max1 = b


    return max1


result = find_max_num(input)
print(result)