a = input()
alpha = [0]*26

for i in a:

    if ord(i)<97:
        alpha[ord(i)-65] += 1
    else:
        alpha[ord(i)-97] += 1
max_alpha = 0
max_alpha_idx = 0

for i in range(len(alpha)):

    if alpha[i] > max_alpha:
        max_alpha = alpha[i]
        max_alpha_idx = i
same = 0
for i in alpha:

    if i == max_alpha:
        same += 1

if same >= 2:
    print('?')
else:
    b = chr(max_alpha_idx+65)
    print(b)

