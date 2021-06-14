finding_target = 18
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    a = len(finding_numbers)

    b = a//2
    d = 0
    while 1:

        if b == 0:
            return False

        if finding_numbers[b] < finding_target:
            c = (a - b)//2 
            print(c)
            b = b + c
            if c == 0:
                d += 1
            
            if d == 1:
                return False
        elif finding_numbers[b] > finding_target: 
            b = b // 2
        elif finding_numbers[b] == finding_target:
            return True
    
        
    


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)