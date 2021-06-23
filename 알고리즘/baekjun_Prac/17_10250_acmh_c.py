n = int(input())
bb = []
for i in range(n):
    a = list(map(int,input().split()))

    c = a[2]//a[0]
    b = a[2]%a[0]

    if b > 0:
        c +=1
    elif b == 0:
        b = a[0]
    
    b = c + b*100
    bb.append(b)

for i in bb:
    print(i)