n_input = int(input())
count_l = []
for i in range(n_input):

    x,y = map(int,input().split())
    if x>y:
        print('x가 y 보다 큽니다.')
        break
    
    l1 = y - x
    a = 1
    count = 0
    
    while True:
        
        if l1 > a*2:
            l1 -= a*2
            count += 2
            a += 1
        else:
            for j in range(a,0,-1):
                if l1 == 0:
                    break
                i = l1//j
                l1 -= i*j
                count += i
            if l1 ==0:
                break
        

    count_l.append(count)         
    
        
for i in range(len(count_l)):
    print(count_l[i])

    