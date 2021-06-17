import sys
a = list(map(int,sys.stdin.readline().rstrip().split()))
b = list(map(int,sys.stdin.readline().rstrip().split()))


am = max(b)
amin = 1


n = (am + 1)//2
while True:
    sum1 = 0
    nn =  n

    for i in b:
        
        if i>n:
            sum1 += i-n
        if sum1 > a[1]:
            break
    
    if sum1 > a[1]:
        amin = n + 1
        n = (am + n + 1)//2
        
    elif sum1 < a[1]:
        
        n = (n+amin)//2
    else:
        print(n)
        break


        
        
    
    



