a = int(input())
b = 0
aa = 0
count = 0
aaa = a

while True:

    b = a//10 + a%10
    aa = (a%10)*10 + b%10
    a = aa
    count += 1

    if aa == aaa:
        
        
        break

print(count)



    
