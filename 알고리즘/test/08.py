word = input()

count = 0 
i = 0

while True:
    if len(word) == 1:
        count += 1
        break
    
    if word[i] == 'c':
        if word[i+1] == '=':
            count +=1
            i += 2
            # print(i)
        elif word[i+1] == '-':
            count +1
            i+=2
        else:
            count += 1
            i += 1
        
    elif word[i] == 'd':
        if word[i+1] == 'z':
            if word[i+2] == '=':
                count += 1
                i += 3
        elif word[i+1] == '-':
            count +=1
            i += 2
        else:
            count += 1
            i += 1
    elif word[i] == 'l':
        if word[i+1] == 'j':
            count +=1
            i += 2
        else:
            count += 1
            i += 1
    elif word[i] == 'n':
        if word[i+1] == 'j':
            count +=1
            i += 2
        else:
            count += 1
            i += 1
    elif word[i] == 's':
        if word[i+1] == '=':
            count +=1
            i += 2
        else:
            count += 1
            i += 1
    elif word[i] == 'z':
        if word[i+1] == '=':
            count +=1
            i += 2
        else:
            count += 1
            i +=1
    else:
        count += 1
        i += 1

    
    if i == len(word):
        break


print(count)