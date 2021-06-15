a = int(input())
b = []
for i in range(a):

    c = list(map(int,input().split()))    
    b.append(c)

for i in range(1, len(b)):
        for j in range(i):
            if b[i - j - 1][1] > b[i - j][1]:
                b[i - j - 1], b[i - j] = b[i - j], b[i - j - 1]                
            elif b[i - j - 1][1] == b[i - j][1]:
                if b[i - j - 1][0] > b[i - j][0]:                    
                    b[i - j - 1], b[i - j] = b[i - j], b[i - j - 1]
            else:
                break
    
    

for x, y in b:
    print(x,y)
    