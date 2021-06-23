word_num = int(input())
group_count = 0 

for i in range(word_num):
    word_input = input()
    word_check = ''
    words = []
    word_check = word_input[0]
    a = 0
    for j in range(len(word_input)):
        
        
        if word_check != word_input[j]:
            
            for k in range(j,len(word_input)):
                if word_check == word_input[k]:
                    a += 1
            if a > 0:
                break 
            word_check = word_input[j]
                
    if a == 0:
        group_count += 1
                    
print(group_count)




        

        
            

