
# 퀵 정렬로 다시 짜보기
 
a = int(input())
b = []
for i in range(a):
    x,y = map(int,input().split())
    if i == 0:
        b.append([x,y])
    else:
        b.append([x,y])
        if b[i-1][1] > y:
            b[i-1], b[i] = b[i-1], b[i]
        


    if b[i]

