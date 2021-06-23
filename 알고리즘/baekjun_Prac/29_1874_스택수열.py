1 2 3 4 5 6 7 8


4 3 6 8 7 5 2 1

안돼는 조건 

가능하려면 x 보다 1 초과 해서 작은 수가 나올려면 
앞에 사이 숫자들이 나와야 한다.

x x-2 false

x-1 x x-2 true

조건을 가지고 로직을 짜자


n = int(input())
a = []
for i in range(n):
    b = int(input())
    a.append(b)
    if len(a) != 0:
        if a[i] < a[i-1]:
            for i in range(a[i-1]-a[i]):