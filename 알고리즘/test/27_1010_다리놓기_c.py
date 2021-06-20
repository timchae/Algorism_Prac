
def fac(n):
    if n == 0:
        return 1
    return n*fac(n-1)

a = int(input())
b = []
for i in range(a):
    x,y = map(int,input().split())
    s = fac(y)//fac(x)//fac(y-x)
    b.append(s)

for i in b:
    print(i)