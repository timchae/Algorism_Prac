# N, M = map(int, input().split())
# tree = list(map(int, input().split()))
# start, end = 1, max(tree) #이분탐색 검색 범위 설정

# while start <= end: #적절한 벌목 높이를 찾는 알고리즘
#     mid = (start+end) // 2
    
#     log = 0 #벌목된 나무 총합
#     for i in tree:
#         if i >= mid:
#             log += i - mid
    
#     #벌목 높이를 이분탐색
#     if log >= M:
#         start = mid + 1
#     else:
#         end = mid - 1
# print(end)


# import sys

# N, M = map(int, sys.stdin.readline().split())
# trees = list(map(int, sys.stdin.readline().split()))

# cut_low = 0
# cut_high = max(trees)
# result = 0
# while cut_high >= cut_low:
#     pivot = (cut_low + cut_high) // 2
#     # pivot의 길이로 자를 수 있는 나무의 총 길이
#     cut_tree = sum([x - pivot if x >= pivot else 0 for x in trees])
#     # 비교
#     if cut_tree >= M:
#         cut_low = pivot + 1
#         # 이 높이로 M이상의 나무를 자를 수 있고, 저장된 정답보다 크다면 이 높이로 정답을 업데이트
#         if result < pivot: result = pivot
#     elif cut_tree < M: cut_high = pivot - 1

# print(result)

    
print(5//2)