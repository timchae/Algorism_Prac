a, a1, a2 =input().split()

a = int(a)
a1 = int(a1)
a2 = int(a2)


b =  a-a1
c = a2-a
i = c/b - int(c/b) 
print(i)
if i > 0:

    count = int(c/b +2)
else:
    count = int(c/b +1)

print(count)