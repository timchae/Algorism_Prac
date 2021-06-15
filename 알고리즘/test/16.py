a = list(map(int,input().split()))

input = 20
max_input = max(a)



prime_list = []

for n in range(2, max_input + 1):
    for i in prime_list:
        if n % i == 0 and i * i <= n:
            break
    else:
        prime_list.append(n)
    
for i in range(len(a)):
    x = a[i]
    for j in range(len(prime_list)):
        
        if x == 0:
            break


        


        


    
