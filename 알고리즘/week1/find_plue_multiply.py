
def find_max_plus_or_multiply(array):
    
    sum1 = 1
    for a in range(len(array)):
        

        if a == 0:
            if array[a] == 0:
                sum1 = 1
            elif array[a] == 1:
                sum1 = 1
            else:
                sum1 *= array[a]
        else:

            if array[a] == 1:
                sum1 += array[a]
            elif array[a] == 0:
                sum1 += array[a]
            else:
                sum1 *= array[a]

        
        
        
    # 이 부분을 채워보세요!
    return sum1

result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))
