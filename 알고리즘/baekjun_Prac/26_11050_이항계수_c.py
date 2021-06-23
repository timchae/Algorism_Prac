
def fac(n):
    if n == 0:
        return 1
    return n*fac(n-1)

a = list(map(int,input().split()))

s = fac(a[0])//fac(a[1])//fac(a[0]-a[1])

print(s)
