a = int(input())
b = []
for i in range(a):
    bb = list(input())
    c = 0
    for j in bb:
        if j == '(':
            c += 1
        else:
            c -= 1
        if c < 0:
            b.append('NO')
            break
        
    if c == 0:
        b.append('YES')
    elif c > 0:
        b.append('NO')

for i in b:
    print(i)

