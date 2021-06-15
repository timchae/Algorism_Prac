

count_n = []
while True:
    count_l = []
    n = int(input())
    if n == 0:
        break
    count = 0
    
    for i in range(n+1,(2*n)+1,1):
        for ii in range(2, i):
            if i % ii == 0:
                break
        else:
            count_l.append(i)

    count_n.append(len(count_l))

for i in range(len(count_n)):
    print(count_n[i])
