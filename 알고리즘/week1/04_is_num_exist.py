input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):

    for a in range(len(array)):
        if array[a] == number:
            return True
        
    # 이 부분을 채워보세요
    return False


result = is_number_exist(7, input)
print(result)