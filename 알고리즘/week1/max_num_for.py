input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    
    for num in array:

        for max_num in array:

            if max_num>num:
                break
        else:
            return num    
        
    return 1


result = find_max_num(input)
print(result)