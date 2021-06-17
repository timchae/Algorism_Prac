input = [4, 6, 3, 5, 2, 9, 1]


def selection_sort(array):
    a = 0
    for i in range(len(array)):
        
        for ii in range(len(array)-i):
            if array[ii+i] < array[i]:
                array[ii+i], array[i] = array[i], array[ii+i]
    # 이 부분을 채워보세요!
    return


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!