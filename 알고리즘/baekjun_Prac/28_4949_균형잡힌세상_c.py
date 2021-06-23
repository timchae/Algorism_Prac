
# res = []
# while True:
#     a = list(input())    
#     r = []    
#     rn = 0
#     b = 0
#     s = 0
#     if a[0] == '.':
#         break
#     for i in range(len(a)):
        
        
#         if a[i] == '(':
#             s += 1
#             r.append(a[i])
#             rn += 1
#         elif a[i] == ')':
#             s -= 1 
#             if s<0:
#                 res.append('no')
#                 break
#             if r[rn-1] == '(':
#                 del r[rn-1]
#                 rn -= 1
#             elif r[rn-1] == '[':
#                 res.append('no')
#                 break           
#         if a[i] == '[':
#             b += 1
#             r.append(a[i])
#             rn += 1
#         elif a[i] == ']':
#             b -= 1
#             if b<0:
#                 res.append('no')
#                 break
#             if r[rn-1] == '[':
#                 del r[rn-1]
#                 rn -= 1
#             elif r[rn-1] == '(':
#                 res.append('no')
#                 break           
#     if r == []:
#         if s>= 0 and b>=0:
#             res.append('yes')

stack = []
left = ["(", "["]
right = [")", "]"] 
valid_set = ["()", "[]"]
res = []
while True:
    isVPS = True
    stack.clear()
    s = input()
    if s==".":
        break
    for j in s:
        if j in left:
            stack.append(j)
        elif j in right:
            if len(stack)!=0:
                tmp = stack.pop()
                if tmp+j not in valid_set:
                    isVPS = False
                    break
            else:
                isVPS = False
                break
    if (isVPS==True) and (len(stack)==0):
        res.append('yes')
    else:
        res.append('no')

for i in res:
    print(i)
 



