t, m = input().split()

t = int(t)
m = int(m)

if m >= 45:
    m -= 45
    
else:
    m -= 45
    m += 60
    t -= 1
    if t < 0:
        t += 24

print(t,m)