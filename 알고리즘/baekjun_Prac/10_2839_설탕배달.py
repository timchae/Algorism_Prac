num_input = int(input())

a_5 = 0
a_3 = 0
less = 0
a_5 = num_input//5
less = num_input%5

while True:
    if less%3 == 0:
        a_3 = less/3
        break
    else:
        a_5 -= 1
        less += 5

    if a_5 < 0:
        break
if a_5 < 0:
    print(-1)
else:
    print(int(a_5+a_3))
