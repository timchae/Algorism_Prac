input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    
    l = len(array)
    
    for i in reversed(range(l)):
        for a in range(i):
            if array[a] > array[a+1]:
                array[a], array[a+1] = array[a+1], array[a]
        
    
    # 이 부분을 채워보세요!
    return 


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!